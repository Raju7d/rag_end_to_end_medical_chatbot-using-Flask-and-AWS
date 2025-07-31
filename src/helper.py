
from typing import List
from langchain.schema import Document
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings


def load_documents(data_path: str) -> List:
    loader = DirectoryLoader(
        data_path, glob="*.pdf", loader_cls=PyPDFLoader
    )
    documents = loader.load()
    return documents


def filter_minimal_docs(docs: List[Document]) -> List[Document]:
    # filer out the docs that are two short

    minimal_docs = []

    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs


# split the data into smaller chunks
def chunk_data(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    text_chunk = text_splitter.split_documents(minimal_docs)
    return text_chunk


# Download embeddings model from the Hugging face (sentence transformer)
def download_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name
    )
    return embeddings