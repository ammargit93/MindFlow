from fastapi import FastAPI, WebSocket, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


metric_route = APIRouter()
templates = Jinja2Templates(directory="templates") 

@metric_route.get("/metrics")
async def get_metrics(request: Request):
    return templates.TemplateResponse("metric.html", {"request": request})

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message received: {data}")
