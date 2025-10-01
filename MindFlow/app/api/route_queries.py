import json
import logging
from collections import Counter
from utils.helper import *

from fastapi import APIRouter, Request
import httpx
from dotenv import load_dotenv, find_dotenv

from app.config import routes
from utils.load_balance import random_balancer

# ------------------ Setup ------------------ #
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv(find_dotenv())

router = APIRouter()


route_count: Counter = Counter()
domain_count: Counter = Counter()


@router.api_route('/', methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def route_query(request: Request):
    # Parse request
    headers = {k.lower(): v for k, v in request.headers.items()}
    method = request.method
    params = dict(request.query_params)
    body_bytes = await request.body()
    body_json = parse_request_body(body_bytes)

    for route in routes:
        if method not in route.methods:
            continue

        # Check required fields in headers or request body/params
        header_match = all(field.lower() in headers for field in route.required_fields)
        source = body_json if method in ["POST", "PUT"] else params
        source_match = all(field in source for field in route.required_fields)

        if header_match or source_match:
            dispatch_url = random_balancer(route.urls)
            domain_count[dispatch_url] += 1
            log_domain_counts(domain_count)

            # Forward request
            async with httpx.AsyncClient() as client:
                try:
                    resp = await client.request(
                        method=method,
                        url=dispatch_url,
                        headers=headers,
                        params=params,
                        content=body_bytes,
                        timeout=10.0  # Add timeout for production readiness
                    )
                    data = resp.json() if "application/json" in resp.headers.get("content-type", "") else resp.text
                except httpx.RequestError as e:
                    logging.error(f"Error forwarding request to {dispatch_url}: {e}")
                    return {"error": f"Failed to reach downstream service at {dispatch_url}"}

            route_count[route.route_name] += 1
            return {
                "matched_route": route.route_name,
                "status": resp.status_code,
                "data": data,
            }

    logging.info("Request did not match any route")
    return {"error": "No matching route found"}
