from langchain_chroma import Chroma

from app.rag.embeddings import get_embeddings


def create_vector_store(chunks):
    """
    Creates and saves the Chroma vector database.
    """

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    print("✅ Vector database created.")

    return vector_store