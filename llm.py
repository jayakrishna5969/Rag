import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_cohere import CohereEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
import asyncio
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain

# Load environment variables from .env file 
load_dotenv()

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

file_path = ("C:/Users/jayakrishna.jajula/Downloads/Jayakrishna (5).pdf")

loader = PyPDFLoader(file_path)
async def load_pages():
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return pages

pages = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(pages)

#text- embeddings

embeddings = CohereEmbeddings(model="embed-english-v3.0")
embedding_dim = len(embeddings.embed_query(pages[0].page_content))
index = faiss.IndexFlatL2(embedding_dim)
# print(pages[0])

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

# Index chunks
_ = vector_store.add_documents(documents=all_splits)

# Create retriever from vector store
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}  # Number of relevant chunks to retrieve
)

# Create RAG chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Function to get response
def get_response(query, chat_history=[]):
    result = qa_chain({"question": query, "chat_history": chat_history})
    return result["answer"]

# Test the RAG system
prompt = "When did Prabhakar completed his B.tech?"
response = get_response(prompt)
print("Response:", response)
