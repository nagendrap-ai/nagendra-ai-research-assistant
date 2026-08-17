from langchain_core.messages import HumanMessage

from app.langchain_llm import invoke_llm
from app.rag.rag import retrieve_context


def answer_pdf_question(question):

    context = retrieve_context(question)

    if context is None:
        return {
            "found": False,
            "answer": None
        }

    prompt = f"""
You are an AI Research Assistant.

Answer ONLY using the context below.

Context:

{context}

Question:

{question}

If the answer is NOT present in the context,
respond ONLY with:

NOT_FOUND
"""

    answer = invoke_llm([
        HumanMessage(content=prompt)
    ])

    # Clean the response
    #answer = answer.strip().replace('"', '')
    # Normalize the response
    answer = answer.strip().replace('"', '').replace("_", " ")

    if "NOT FOUND" in answer.upper():
        return{
            "found": False,
            "answer": None
        }
    return {
        "found": True,
        "answer": answer
    }