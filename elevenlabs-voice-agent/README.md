# ElevenLabs voice agent

[← AI Engineer](../README.md)

## What

A live voice agent for a clinic front desk. You speak, the agent answers, and it calls client-side tools to look up patient records and book appointments.

| File | Role |
| :--- | :--- |
| `main.py` | Opens a conversation with your ElevenLabs agent and wires the microphone and speaker |
| `patient_records.py` | The patient lookup the agent calls |
| `setup_tools.py` | Registers the tools with your ElevenLabs agent |
| `Makefile` | `install`, `setup`, `tools`, `run` |

## Run

```bash
cd elevenlabs-voice-agent
make setup      # installs PortAudio and Python packages, creates .env
# Add ELEVENLABS_API_KEY and ELEVENLABS_AGENT_ID to .env
make tools      # registers the tools
make run        # starts the conversation
```

## Article

Coming soon.

## Depends on

- An ElevenLabs account with a Conversational AI agent.
- A microphone and speakers.
- PortAudio (`make install` handles macOS, Linux, and Windows).
