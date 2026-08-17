from app.rag.retriever import retrieve_documents


def retrieve_context(question: str):
    """
    Retrieves relevant context from the vector database.
    Returns None if no documents are found.
    """

    documents = retrieve_documents(question)

    if not documents:
        print("❌ No documents found.")
        return None

    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    #print(f"✅ Retrieved {len(documents)} document(s).")

    return context