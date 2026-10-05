"""
Registers client tools on the ElevenLabs agent via the API.
Run once: python setup_tools.py
"""

import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.types import (
    AgentConfig,
    ConversationalConfig,
    LiteralJsonSchemaProperty,
    ObjectJsonSchemaPropertyOutput,
    PromptAgentApiModelOutput,
    PromptAgentApiModelOutputToolsItem_Client,
)

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")


def str_param(description: str) -> LiteralJsonSchemaProperty:
    return LiteralJsonSchemaProperty(type="string", description=description)


tools = [
    PromptAgentApiModelOutputToolsItem_Client(
        name="get_patient_record",
        description=(
            "Look up a patient's record by their full name or patient ID. "
            "Call this as soon as the caller provides their name or patient ID."
        ),
        expects_response=True,
        parameters=ObjectJsonSchemaPropertyOutput(
            type="object",
            properties={
                "name": str_param("Full name of the patient, e.g. 'John Smith'"),
                "patient_id": str_param("Patient ID, e.g. 'P001'"),
            },
        ),
    ),
    PromptAgentApiModelOutputToolsItem_Client(
        name="save_booking",
        description=(
            "Save the confirmed appointment once the patient's name and appointment "
            "time are both confirmed."
        ),
        expects_response=True,
        parameters=ObjectJsonSchemaPropertyOutput(
            type="object",
            required=["name", "appointment_time"],
            properties={
                "name": str_param("Patient's full name"),
                "appointment_time": str_param(
                    "Confirmed date and time, e.g. '2026-03-17 09:30 AM'"
                ),
            },
        ),
    ),
]

if __name__ == "__main__":
    # Preserve existing agent config, only patch in new tools
    agent = client.conversational_ai.agents.get(agent_id=AGENT_ID)
    a = agent.conversation_config.agent
    existing_prompt = a.prompt

    updated = client.conversational_ai.agents.update(
        agent_id=AGENT_ID,
        conversation_config=ConversationalConfig(
            agent=AgentConfig(
                first_message=a.first_message,
                language=a.language,
                prompt=PromptAgentApiModelOutput(
                    prompt=existing_prompt.prompt,
                    llm=existing_prompt.llm,
                    tools=tools,
                ),
            )
        ),
    )

    print("Agent updated. Tools registered:")
    for t in updated.conversation_config.agent.prompt.tools:
        print(f"  - {t.name} (type={t.type}, expects_response={t.expects_response})")
