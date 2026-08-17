from langchain_core.messages import HumanMessage

from app.langchain_llm import invoke_llm


def summarize_search_results(question, search_results):

    prompt = f"""
You are an AI Research Assistant.

User Question:
{question}

Search Results:
{search_results}

Answer the user's question using ONLY the search results provided.

If the search results do not contain enough information, clearly say so.

Provide a concise and well-formatted answer.
"""

    return invoke_llm([
        HumanMessage(content=prompt)
    ])