from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec
from src.helper import load_documents, filter_minimal_docs, chunk_data, download_embeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

pinecone_api_key = os.getenv("PINECONE_API_KEY")
print(f'Pine cone api key: {pinecone_api_key}')

extracted_documents = load_documents("data/")
print(f'length of the extracted documents: {len(extracted_documents)}')

minimal_docs = filter_minimal_docs(extracted_documents)
print(f'length of minimal_docs: {len(minimal_docs)}')

chunked_data = chunk_data(minimal_docs)
print(f'length of chunked data: {chunked_data}')

embedding = download_embeddings()


# create a pinecone client
pc = Pinecone(api_key=pinecone_api_key)
print(f'Pinecone client: {pc}')

# Create pinecone index
index_name = "medical-chatbot"
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
# create index
index = pc.Index(index_name)


# pine index has been created successfully. now we need to store the vectors in Pinecone vector db
# docsearch will convert chunked_data into embeddings and store them into pinecone vector db
docs_earch = PineconeVectorStore.from_documents(
    documents=chunked_data,
    embedding=embedding,
    index_name=index_name
)