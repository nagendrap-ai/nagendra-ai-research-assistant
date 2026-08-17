from app.rag.embeddings import get_embeddings


# Session vector store
_uploaded_vector_store = None


def set_uploaded_vector_store(vector_store):
    """
    Stores the uploaded PDF vector store
    in memory.
    """

    global _uploaded_vector_store

    _uploaded_vector_store = vector_store

    print("✅ Uploaded vector store ready.")


def clear_uploaded_vector_store():
    """
    Clears uploaded PDF vector store.
    """

    global _uploaded_vector_store

    _uploaded_vector_store = None

    print("🗑️ Uploaded vector store cleared.")


def get_vector_store():
    """
    Returns the uploaded PDF vector store.

    Returns None when no PDF has been uploaded.
    """

    if _uploaded_vector_store is None:

        print("ℹ️ No uploaded PDF vector store available.")

        return None

    return _uploaded_vector_store


def reset_vector_store():

    global _uploaded_vector_store

    _uploaded_vector_store = None
