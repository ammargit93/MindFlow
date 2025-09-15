from fastapi import APIRouter
from app.config import indices
import math


router = APIRouter()

class LLMInvoker:
    def __init__(self, model_card):
        pass

@router.get("/")
def route_query(query: str):
    best_index = None
    min_dist = math.inf
     
    for index in indices:
        res = index.query_document(query) 
        avg_dist = sum(res['distances'][0]) / len(res['distances'][0])
        
        if avg_dist < min_dist:
            min_dist = avg_dist
            best_index = index
    
    llm = best_index.llm
    
    return {"best_index": best_index.index_name, "distance": min_dist, "LLM":llm}
        
