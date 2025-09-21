from fastapi import APIRouter
from app.config import routes
from dotenv import load_dotenv, find_dotenv
import math


env_path = find_dotenv()
load_dotenv(env_path)


router = APIRouter()


@router.get("/")
def route_query(query: str):
    best_route = None
    min_dist = math.inf
    for route in routes:
        res = route.index.query_document(query) 
        avg_dist = res['distance']
        if avg_dist < min_dist:
            min_dist = avg_dist
            best_route = route
    
    return {
        "distance":min_dist, 
        "route":best_route.index.index_name, 
    }
        

