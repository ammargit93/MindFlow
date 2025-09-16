from utils.load_yaml import load_config
from index.chroma import ChromaIndex
from route.routes import Route
import uuid

cfg = load_config()['routes']
routes = []


class RouteIndex:
    def __init__(self, Route, ChromaIndex):
        self.route = Route
        self.index = ChromaIndex
        
        
for config in cfg:
    collection_name = config['name']
    document = config['utterances']
    llm = config['model_id'].split(":")[-1]
    inference_provider = config['inference_provider']
    api_url = config['api_url']
    
    route = Route(route_name=collection_name, model_card=llm, inference_provider=inference_provider, api_url=api_url)
    chroma_index = ChromaIndex(collection_name=collection_name, llm=llm)
    route_index = RouteIndex(route, chroma_index)
    
    chroma_index.add_document(documents=document, ids=[str(uuid.uuid1()) for _ in document])
    routes.append(route_index)
        