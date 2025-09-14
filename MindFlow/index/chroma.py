import chromadb
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings


class BaseIndex:
    def __init__(self, collection_name):
        client = chromadb.Client()
        self.collection = client.create_collection(collection_name)

    
    
class ChromaIndex(BaseIndex):
    def __init__(self, collection_name):
        self.index_name = collection_name
        super().__init__(collection_name)
        
        
    def add_document(self, documents,ids,metadata=None):
        embeddings = FastEmbedEmbeddings()
        document_embeddings = embeddings.embed_documents(documents)
        self.collection.add(
            documents=documents,
            embeddings=document_embeddings,
            metadatas=metadata,            
            ids=ids
        )
        
    
    def query_document(self, query):
        embedding = FastEmbedEmbeddings()
        embedded_query = embedding.embed_query(query)
        return self.collection.query(query_embeddings=embedded_query,query_texts=query)
    
    
    def clear_index(self):
        self.collection.delete()