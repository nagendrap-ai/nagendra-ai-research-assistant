from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    """
    Loads a PDF and returns a list of LangChain Document objects.
    """

    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        print(f"✅ Loaded {len(documents)} pages.")

        return documents

    except Exception as e:
        print(f"❌ Error loading PDF: {e}")
        return []