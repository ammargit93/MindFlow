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
    print(headers)
    print(method)
    return {'key':'value'}
