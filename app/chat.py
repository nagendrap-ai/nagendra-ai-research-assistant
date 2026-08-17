from langchain_core.messages import SystemMessage

from app.memory import ConversationMemory
from app.prompts import SYSTEM_PROMPT
from app.langchain_llm import invoke_llm

memory = ConversationMemory()

def ask_chat(question: str):

    # Store the user's message
    memory.add_user_message(question)

    # Build the conversation
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *memory.get_messages()
    ]

    # Send all messages to the LLM
    response = invoke_llm(messages)

    # Store the AI response
    memory.add_ai_message(response)

    return response
