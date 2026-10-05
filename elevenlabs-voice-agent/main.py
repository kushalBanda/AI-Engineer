import json
import os
import queue
import signal
import struct
import threading

import pyaudio
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import (
    AudioInterface,
    ClientTools,
    Conversation,
    ConversationInitiationData,
)

from patient_records import lookup

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")

client = ElevenLabs(api_key=API_KEY)


# ---------------------------------------------------------------------------
# Booking store — populated by the agent via client tool
# ---------------------------------------------------------------------------

booking: dict = {}


def handle_get_patient_record(params: dict) -> str:
    record = lookup(name=params.get("name"), patient_id=params.get("patient_id"))
    print(f"\n[tool] get_patient_record({params}) → {record}\n")
    return json.dumps(record)


def handle_save_booking(params: dict) -> str:
    booking.update(params)
    print(f"\n[tool] save_booking → {booking}\n")
    return f"Booking confirmed for {params.get('name')} on {params.get('appointment_time')}."


# ---------------------------------------------------------------------------
# Audio interface — MacBook mic (48kHz→16kHz) + system default output
# ---------------------------------------------------------------------------

def _downsample(data: bytes, from_rate: int, to_rate: int) -> bytes:
    """Decimate audio by integer ratio (e.g. 48000→16000 = step 3)."""
    step = from_rate // to_rate
    samples = struct.unpack(f"<{len(data) // 2}h", data)
    decimated = samples[::step]
    return struct.pack(f"<{len(decimated)}h", *decimated)


class SplitAudioInterface(AudioInterface):
    INPUT_DEVICE_INDEX = 2    # MacBook Air Microphone — native 48kHz
    INPUT_RATE = 48000
    OUTPUT_DEVICE_INDEX = None  # System default
    OUTPUT_RATE = 16000
    CHUNK = 4800              # 100ms at 48kHz
    ECHO_TAIL_MS = 300        # keep mic muted this long after agent stops speaking

    def start(self, input_callback):
        self._pa = pyaudio.PyAudio()
        self._output_queue: queue.Queue[bytes] = queue.Queue()
        self._stop = threading.Event()
        self._agent_speaking = threading.Event()
        self._echo_tail_timer: threading.Timer | None = None

        def _in_callback(data, _frame_count, _time_info, _status):
            if not self._agent_speaking.is_set():
                input_callback(_downsample(data, self.INPUT_RATE, self.OUTPUT_RATE))
            return (None, pyaudio.paContinue)

        self._in_stream = self._pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.INPUT_RATE,
            input=True,
            input_device_index=self.INPUT_DEVICE_INDEX,
            frames_per_buffer=self.CHUNK,
            stream_callback=_in_callback,
        )
        self._out_stream = self._pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.OUTPUT_RATE,
            output=True,
            output_device_index=self.OUTPUT_DEVICE_INDEX,
            frames_per_buffer=self.OUTPUT_RATE // 10,
        )
        self._out_thread = threading.Thread(target=self._drain_output, daemon=True)
        self._out_thread.start()

    def stop(self):
        self._stop.set()
        self._out_thread.join()
        self._in_stream.stop_stream()
        self._in_stream.close()
        self._out_stream.close()
        self._pa.terminate()

    def output(self, audio: bytes):
        self._agent_speaking.set()
        self._cancel_echo_tail()
        self._output_queue.put(audio)

    def interrupt(self):
        self._cancel_echo_tail()
        self._agent_speaking.clear()
        # Drain all queued audio at once
        with self._output_queue.mutex:
            self._output_queue.queue.clear()

    def _cancel_echo_tail(self):
        if self._echo_tail_timer is not None:
            self._echo_tail_timer.cancel()
            self._echo_tail_timer = None

    def _drain_output(self):
        while not self._stop.is_set():
            try:
                self._out_stream.write(self._output_queue.get(timeout=0.1))
            except queue.Empty:
                # Queue drained — start the mute tail only if no timer is pending
                if self._agent_speaking.is_set() and self._echo_tail_timer is None:
                    self._echo_tail_timer = threading.Timer(
                        self.ECHO_TAIL_MS / 1000, self._agent_speaking.clear
                    )
                    self._echo_tail_timer.start()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"Connecting to agent: {AGENT_ID}")
    print("Speak into your mic. Press Ctrl+C to stop.\n")

    client_tools = ClientTools()
    client_tools.register("get_patient_record", handle_get_patient_record)
    client_tools.register("save_booking", handle_save_booking)

    conversation = Conversation(
        client=client,
        agent_id=AGENT_ID,
        requires_auth=API_KEY is not None,
        audio_interface=SplitAudioInterface(),
        client_tools=client_tools,
        config=ConversationInitiationData(
            conversation_config_override={
                "agent": {"tts": {"output_format": "pcm_16000"}}
            }
        ),
        callback_agent_response=lambda text: print(f"Agent: {text}"),
        callback_user_transcript=lambda text: print(f"You:   {text}"),
    )

    def _shutdown(_sig, _frame):
        print("\nEnding conversation...")
        conversation.end_session()

    signal.signal(signal.SIGINT, _shutdown)

    conversation.start_session()
    conversation.wait_for_session_end()

    if booking:
        print(f"\nBooking summary: {json.dumps(booking, indent=2)}")
    else:
        print("\nNo booking was saved this session.")


if __name__ == "__main__":
    main()
