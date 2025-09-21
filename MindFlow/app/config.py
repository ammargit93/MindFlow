from utils.load_yaml import load_config
from index.chroma import ChromaIndex
from index.faiss import FAISSIndex
from route.routes import Route
import uuid

loaded = load_config()

route_cfg = loaded['routes']
default_cfg = loaded['defaults']


routes = []

DEFAULT_CFG_MAPPER = {
    "chroma": ChromaIndex,
    "faiss": FAISSIndex
}

class RouteIndex:
    def __init__(self, Route, Index):
        self.route = Route
        self.index = Index
        
        
for config in route_cfg:
    collection_name = config['name']
    document = config['utterances']
    api_url = config['api_url']
    
    route = Route(route_name=collection_name, api_url=api_url)
    
    general_index = DEFAULT_CFG_MAPPER[default_cfg["vectordb"]](collection_name=collection_name)
    
    route_index = RouteIndex(route, general_index)
    
    general_index.add_document(documents=document)
    
    routes.append(route_index)
        