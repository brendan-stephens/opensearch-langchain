from typing import List
from langchain.schema import Document                   # The main LangChain library for chaining models together.
from langchain_huggingface import HuggingFaceEmbeddings # The Hugging Face embeddings for generating embeddings.
from langchain_community.vectorstores import OpenSearchVectorSearch
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Ingest documents into OpenSearch.")
parser.add_argument("--opensearch_url", required=True, help="OpenSearch URL to connect to")
args = parser.parse_args()

# Use the opensearch_url in your script
print(f"Using OpenSearch URL: {args.opensearch_url}")

# Initialize Hugging Face embeddings
model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# Define Hugging Face embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"  # Example embedding model
)

# Raw data as documents
docs: List[Document] = [
    Document(page_content="Hello World!", metadata={"sentiment": "positive", "source": "abc.txt"}),
    Document(page_content="If you want to live a happy life, tie it to a goal, not to people or things.", metadata={"author": "A. Einstein"}),
    Document(page_content="Not how long, but how well you have lived is the main thing.", metadata={"author": "Seneca"}),
]

print(f"Generate Embeddings...")

# Data ingestion into OpenSearch vector db
docsearch = OpenSearchVectorSearch.from_documents(
    docs,
    embeddings,
    opensearch_url=args.opensearch_url,
    index_name="vector",
    engine="faiss",
    bulk_size=50  # Example bulk size; adjust as needed
)

# Test the vector db
query = "Hi World"
print(f"Vector Query: {query}")

retrieved_docs = docsearch.similarity_search(query)

# Print the most similar document
print(f"Results: {retrieved_docs[0].page_content}")