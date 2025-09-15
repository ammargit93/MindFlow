from utils.load_yaml import load_config
from index.chroma import ChromaIndex
from app import app
from app.config import indices
import math

@app.get("/mindflow/api/")
def route_query(query: str):
    best_index = None
    min_dist = math.inf

    for index in indices:
        res = index.query_document(query)
        avg_dist = sum(res['distances'][0]) / len(res['distances'][0])
        
        if avg_dist < min_dist:
            min_dist = avg_dist
            best_index = index.index_name

    return {"best_index": best_index, "distance": min_dist}
        
