from fastapi import FastAPI
from utils.load_yaml import load_config
from app.api.route_queries import router
from app.api.metrics_route import metric_route
import logging

cfg = load_config()['routes']
logging.info("Loaded YAML configurations")
app = FastAPI(title="A semantic router")

app.include_router(router=router, prefix="/mindflow/router")
app.include_router(router=metric_route, prefix="/mindflow")