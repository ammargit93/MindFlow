import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_core.documents import Document
import uuid


# MAPPING:
#
# collection -> List[uuid]
#
# 


index_map = {}

def faiss_response_parser(results):
    response = {}
    id = results[0][0].id
    indexname = ""
    for k, v in index_map.items():
        if id in v:
            indexname = k
    
    response['distance'] = float(results[0][1])
    response['index'] = "faiss"    
    
    return response


class FAISSIndex:
    def __init__(self, collection_name, llm):
        self.index_name = collection_name
        self.embeddings = FastEmbedEmbeddings()
        self.index = faiss.IndexFlatL2(len(self.embeddings.embed_query("test")))
        self.vector_store = FAISS(
            embedding_function=self.embeddings,
            index=self.index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )
    
    def add_document(self, documents):
        ids = [str(uuid.uuid1()) for _ in documents]
        document_collection = [Document(page_content=document) for document in documents] 
        index_map[self.index_name] = ids
        self.vector_store.add_documents(documents=document_collection, ids=ids)

    def query_document(self, query):
        results = self.vector_store.similarity_search_with_score(query, k=1)
        response = faiss_response_parser(results=results)
        return response