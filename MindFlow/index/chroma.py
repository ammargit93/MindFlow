import chromadb
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
import uuid



# response format: {
#     llm: LLM that is called,
#     distance: average distance.
#     index: Vector index class that was called,
#     route: Route name (chitchat, politics etc)
# }


def chroma_response_parser(result, llm):
    response = {}
    response['llm'] = llm
    response['distance'] = sum(result['distances'][0])/len(result['distances'][0])
    response['index'] = "chroma"
    
    return response
    
class BaseIndex:
    def __init__(self, collection_name):
        client = chromadb.Client()
        self.collection = client.create_collection(collection_name)

    
    
class ChromaIndex(BaseIndex):
    def __init__(self, collection_name, llm):
        self.index_name = collection_name
        self.llm = llm
        super().__init__(collection_name)
        
        
    def add_document(self, documents):
        ids = [str(uuid.uuid1()) for _ in documents]
        metadata = None
        embeddings = FastEmbedEmbeddings()
        document_embeddings = embeddings.embed_documents(documents)
        self.collection.add(
            documents=documents,
            embeddings=document_embeddings,
            metadatas=metadata,            
            ids=ids
        )
        
    
    def query_document(self, query):
        response = {}
        embedding = FastEmbedEmbeddings()
        embedded_query = embedding.embed_query(query)
        result = self.collection.query(query_embeddings=embedded_query,query_texts=query)
        print(result)
        response = chroma_response_parser(result=result, llm=self.llm)
        return response

    
    
    def clear_index(self):
        self.collection.delete()