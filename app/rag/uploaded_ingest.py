import tempfile
import os

from langchain_chroma import Chroma

from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.embeddings import get_embeddings


def ingest_uploaded_pdf(uploaded_file):
    """
    Creates an in-memory Chroma vector store
    from an uploaded PDF.
    """

    if uploaded_file is None:
        return None

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.getbuffer())

        temp_pdf = tmp.name

    try:

        print("📖 Loading uploaded PDF...")

        documents = load_pdf(temp_pdf)

        print("✂ Splitting...")

        chunks = split_documents(documents)

        print("🧠 Creating embeddings...")

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=get_embeddings()
        )

        print("✅ Uploaded PDF indexed.")

        return vector_store

    finally:

        if os.path.exists(temp_pdf):
            os.remove(temp_pdf)