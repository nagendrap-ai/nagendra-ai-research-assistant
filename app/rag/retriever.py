from app.rag.store import get_vector_store


def retrieve_documents(question: str, k: int = 3):
    """
    Retrieves the top-k most similar documents.
    """

    vector_store = get_vector_store()

    documents = vector_store.similarity_search(
        question,
        k=k
    )

    print(f"✅ Retrieved {len(documents)} document(s).")

    return documents