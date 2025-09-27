import json
from fastapi import APIRouter, Request
from app.config import routes
from dotenv import load_dotenv, find_dotenv
from utils.load_balance import random_balancer
import httpx
import logging

logging.basicConfig(level=logging.INFO, format='\n%(asctime)s - %(levelname)s - %(message)s\n')

env_path = find_dotenv()
load_dotenv(env_path)

router = APIRouter()


route_count = {}
domain_count = {}

@router.api_route('/', methods=["GET","POST","PUT","DELETE","PATCH"])
async def route_query(request: Request):
    headers = {k.lower(): v for k, v in request.headers.items()}
    method = request.method
    params = dict(request.query_params)
    body_bytes = await request.body()
    body_json = json.loads(body_bytes.decode()) if body_bytes else {}

    for route in routes:
        if method not in route.methods:
            continue

        header_match = all(field.lower() in headers for field in route.required_fields)

        source = body_json if method in ["POST", "PUT"] else params
        source_match = all(field in source for field in route.required_fields)

        dispatch_url = random_balancer(route.urls)
        domain_count[dispatch_url] = domain_count.get(dispatch_url, 0) + 1
        logging.info(f"Number of requests in {dispatch_url}: {domain_count[dispatch_url]}")

        if header_match or source_match:
            async with httpx.AsyncClient() as client:
                resp = await client.request(
                    method=method,
                    url=dispatch_url,
                    headers=headers,
                    params=params,
                    content=body_bytes,
                )
            
            logging.info(f"INFO: response from {route.urls[0]}")
            route_count[route.route_name] = route_count.get(route.route_name, 0) + 1
            logging.info(f"Number of requests in {route.route_name}: {route_count[route.route_name]}")
            
            return {
                "matched_route": route.route_name,
                "status": resp.status_code,
                "data": resp.json() if "application/json" in resp.headers.get("content-type","") else resp.text,
            }
    
    logging.info(f"INFO: request did not match any route")
    
    return {"error": "did not match any route"}
