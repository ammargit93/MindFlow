from fastapi import APIRouter, Request
from app.config import routes
from dotenv import load_dotenv, find_dotenv


env_path = find_dotenv()
load_dotenv(env_path)


router = APIRouter()

@router.api_route('/')
def route_query(request: Request):
    headers = request.headers
    method = request.method
   
   
    header_list = set()
    for h in dict(headers):
        header_list.add(h)
        
    for route in routes:
        required_fields = set(route.required_fields)
        methods = set(route.methods)
        
        
        if required_fields & header_list and set(method) & methods:
            
            return {"route":route.route_name}
        else:
            return {"error":"did not match any route"}
            
