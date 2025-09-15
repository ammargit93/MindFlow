from fastapi import FastAPI
from utils.load_yaml import load_config
from app.api.route_queries import router

cfg = load_config()['routes']

app = FastAPI(title="A semantic router")

app.include_router(router=router, prefix="/mindflow/api")
