import json
from fastapi import APIRouter, Request
from app.config import routes
from dotenv import load_dotenv, find_dotenv
import httpx

env_path = find_dotenv()
load_dotenv(env_path)

router = APIRouter()

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

        # Check headers first
        header_match = all(field.lower() in headers for field in route.required_fields)

        source = body_json if method in ["POST", "PUT"] else params
        source_match = all(field in source for field in route.required_fields)

        if header_match:
            async with httpx.AsyncClient() as client:
                resp = await client.request(
                    method=method,
                    url=route.url,
                    headers=headers,
                    params=params,
                    content=body_bytes,
                )
            return {
                "matched_route": route.route_name,
                "status": resp.status_code,
                "data": resp.json() if "application/json" in resp.headers.get("content-type","") else resp.text,
            }

    return {"error": "did not match any route"}
