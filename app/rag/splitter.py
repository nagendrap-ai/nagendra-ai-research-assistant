from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Splits LangChain Document objects into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Created {len(chunks)} chunks.")

    return chunks