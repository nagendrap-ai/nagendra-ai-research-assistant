import os
import shutil

from app.config import PDF_FOLDER
from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.store import get_vector_store


def ingest_pdfs():
    """
    Reads all PDFs from PDF_FOLDER and creates a fresh ChromaDB.
    """

    if not PDF_FOLDER:
        print("❌ PDF_FOLDER is not configured in .env")
        return

    if not os.path.exists(PDF_FOLDER):
        print(f"❌ Folder not found: {PDF_FOLDER}")
        return

    pdf_files = [
        os.path.join(PDF_FOLDER, file)
        for file in os.listdir(PDF_FOLDER)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:
        print("❌ No PDF files found.")
        return

    print(f"\n📂 Reading PDFs from: {PDF_FOLDER}")
    print(f"✅ Found {len(pdf_files)} PDF(s)\n")

    # Delete old vector database
    if os.path.exists("vector_db"):
        print("🗑 Removing old vector database...")
        shutil.rmtree("vector_db")

    all_documents = []

    for pdf in pdf_files:
        print(f"📖 Loading {os.path.basename(pdf)}")

        docs = load_pdf(pdf)

        all_documents.extend(docs)

    print("\n✂ Splitting documents...")

    chunks = split_documents(all_documents)

    print("\n🧠 Creating embeddings...")

    vector_store = get_vector_store()

    vector_store.add_documents(chunks)

    print("\n✅ Knowledge Base updated successfully!")