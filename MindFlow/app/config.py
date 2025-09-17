from utils.load_yaml import load_config
from index.chroma import ChromaIndex
from index.faiss import FAISSIndex
from route.routes import Route
import uuid

loaded = load_config()

route_cfg = loaded['routes']
default_cfg = loaded['defaults']

routes = []


class RouteIndex:
    def __init__(self, Route, FAISSIndex):
        self.route = Route
        self.index = FAISSIndex
        
        
for config in route_cfg:
    collection_name = config['name']
    document = config['utterances']
    llm = config['model_id'].split(":")[-1]
    inference_provider = config['inference_provider']
    api_url = config['api_url']
    
    route = Route(route_name=collection_name, model_card=llm, inference_provider=inference_provider, api_url=api_url)
    # chroma_index = ChromaIndex(collection_name=collection_name, llm=llm)
    
    faiss_index = FAISSIndex(collection_name=collection_name,llm=llm)
    route_index = RouteIndex(route, faiss_index)
    
    # chroma_index.add_document(documents=document, ids=[str(uuid.uuid1()) for _ in document])
    faiss_index.add_document(documents=document)
    routes.append(route_index)
        