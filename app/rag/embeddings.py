from langchain_huggingface import HuggingFaceEmbeddings

# Singleton instance
_embeddings = None


def get_embeddings():
    """
    Returns a singleton HuggingFace embedding model.
    """

    global _embeddings

    if _embeddings is None:

        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        print("✅ Embedding model loaded.")

    return _embeddings