from fastapi import APIRouter
from app.config import routes
import math
from dotenv import load_dotenv, find_dotenv
import os
from huggingface_hub import InferenceClient

env_path = find_dotenv()
load_dotenv(env_path)


router = APIRouter()

# API Inference client
class HFChatCompletionClient:
    def __init__(self, model_card, inference_provider, api_url):
        self.model_card = model_card
        self.inference_provider = inference_provider
        self.api_url = api_url
        self.client = InferenceClient(provider=self.inference_provider, api_key=os.getenv('HF_TOKEN'))


    def invoke(self, query):
        completion = self.client.chat.completions.create(
            model=self.model_card,
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ],
        )
        return completion.choices[0].message




@router.get("/")
def route_query(query: str):
    best_route = None
    min_dist = math.inf
     
    for route in routes:
        index = route.index
        res = index.query_document(query) 
        avg_dist = sum(res['distances'][0]) / len(res['distances'][0])
        
        if avg_dist < min_dist:
            min_dist = avg_dist
            best_route = route
    
    chat_client = HFChatCompletionClient(best_route.index.llm, best_route.route.inference_provider,best_route.route.api_url)
    response = chat_client.invoke(query=query)
    return {"result":response, "llm":best_route.index.llm}
        
