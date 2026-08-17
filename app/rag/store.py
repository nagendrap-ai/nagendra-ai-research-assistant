from langchain_chroma import Chroma

from app.rag.embeddings import get_embeddings

# Persistent vector store (legacy)
_vector_store = None

# Session vector store (uploaded PDF)
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


def get_vector_store():
    """
    Returns uploaded vector store
    if available.

    Otherwise returns persistent vector_db.
    """

    global _vector_store

    # Highest priority
    if _uploaded_vector_store is not None:

        return _uploaded_vector_store

    # Legacy support
    if _vector_store is None:

        _vector_store = Chroma(
            persist_directory="vector_db",
            embedding_function=get_embeddings(),
        )

        print("✅ Persistent Vector Store loaded.")

    return _vector_store


def reset_vector_store():

    global _vector_store

    _vector_store = None