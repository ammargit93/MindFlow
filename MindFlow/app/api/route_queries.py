from fastapi import APIRouter
from app.config import routes
import math
from dotenv import load_dotenv, find_dotenv
import os
from interface import HFChatCompletionClient


env_path = find_dotenv()
load_dotenv(env_path)


router = APIRouter()


@router.get("/")
def route_query(query: str):
    best_route = None
    min_dist = math.inf
    best_response = None
    for route in routes:
        index = route.index
        res = index.query_document(query) 
        avg_dist = res['distance']
        # print(res)
        if avg_dist < min_dist:
            min_dist = avg_dist
            best_route = route
            best_response = res
    
    chat_client = HFChatCompletionClient(best_route.index.llm, best_route.route.inference_provider,best_route.route.api_url)
    response = chat_client.invoke(query=query)
    return {"response":response, "distance":min_dist, "route":best_route.index.index_name, "index":best_response['index'],"llm":best_response['llm']}
        
