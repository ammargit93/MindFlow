from utils.load_yaml import load_config
from index.chroma import ChromaIndex
from fastapi import FastAPI
import logging
import uuid
import time
import math

cfg = load_config()['routes']

app = FastAPI()

indices = []

for config in cfg:
    collection_name = config['name']
    document = config['utterances']
    llm = config['action'].split(":")[-1]
    
    chroma_index = ChromaIndex(collection_name=collection_name)
    chroma_index.add_document(documents=document, ids=[str(uuid.uuid1()) for _ in document])
    indices.append(chroma_index)
        

@app.get("/mindflow/api/")  
def route_query(query: str):
    idxs = []
    min_dist = math.inf
    for index in indices:
        res = index.query_document(query)
        avg_dist = sum(res['distances'][0])/len(res['distances'][0])
        idxs.append((index.index_name, avg_dist))
        min_dist = min(min_dist, avg_dist)
        
    for name, dist in idxs:
        if min_dist == dist:
            return name
        

    
    


