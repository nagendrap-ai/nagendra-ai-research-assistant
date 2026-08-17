from langchain_openai import ChatOpenAI

from app.config import (
    OPENROUTER_API_KEY,
    MODEL_NAME
)

llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def invoke_llm(messages):
    """
    Sends a list of LangChain messages to the LLM
    and returns only the response text.
    """
    response = llm.invoke(messages)
    return response.content