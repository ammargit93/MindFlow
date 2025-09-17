import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_core.documents import Document

import uuid

index_map = {}

class FAISSIndex:
    def __init__(self, collection_name, llm):
        self.index_name = collection_name
        self.llm = llm
        self.embeddings = FastEmbedEmbeddings()
        self.index = faiss.IndexFlatL2(len(self.embeddings.embed_query("test")))
        self.vector_store = FAISS(
            embedding_function=self.embeddings,
            index=self.index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )
    
    def add_document(self, documents):
        document_collection = [Document(page_content=document) for document in documents] 
        
        self.vector_store.add_documents(documents=document_collection, ids=[uuid.uu])

    def query_document(self, query):
        response = {}
        results = self.vector_store.similarity_search_with_score(query, k=1)
        print(results)
        response['res'] = results[0].page_content
        response['score'] = results[1]
        return response