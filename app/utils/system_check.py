import sys
import chromadb
import langchain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai

def test_dependencies():
    results = {
        "ChromaDB Version": chromadb.__version__,
        "LangChain Version": langchain.__version__,
        "Python Version": sys.version,
        "OpenAI SDK Version": openai.__version__
    }
    return results

def test_chroma_functionality():
    try:
        # Initialize ChromaDB client
        client = chromadb.Client()
        
        # Create a test collection
        collection = client.create_collection(name="test_collection")
        
        # Add some test documents
        collection.add(
            documents=["This is a test document"],
            metadatas=[{"source": "test"}],
            ids=["1"]
        )
        
        # Perform a test query
        results = collection.query(
            query_texts=["test document"],
            n_results=1
        )
        
        # Delete test collection
        client.delete_collection("test_collection")
        
        return "ChromaDB functionality test: Passed"
    except Exception as e:
        return f"ChromaDB functionality test: Failed - {str(e)}"

def test_langchain_integration():
    try:
        # Initialize components
        embeddings = OpenAIEmbeddings()
        splitter = RecursiveCharacterTextSplitter()
        
        return "LangChain integration test: Passed"
    except Exception as e:
        return f"LangChain integration test: Failed - {str(e)}"

if __name__ == "__main__":
    # Run tests
    print("\nTesting RAG Components:")
    print("-" * 50)
    
    # Test dependencies
    versions = test_dependencies()
    for component, version in versions.items():
        print(f"{component}: {version}")
    
    print("\nFunctionality Tests:")
    print("-" * 50)
    print(test_chroma_functionality())
    print(test_langchain_integration())