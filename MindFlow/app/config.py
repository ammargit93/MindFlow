from utils.load_yaml import load_config
from route.routes import Route
import uuid

loaded = load_config()

route_cfg = loaded['routes']


routes = []

for config in route_cfg:
    url = route_cfg[config]['url']
    type = route_cfg[config]['type']
    methods = route_cfg[config]['methods']
    trigger_field = route_cfg[config]['trigger_field']
    required_fields = route_cfg[config]['required_fields']
    
    route = Route(url=url, methods=methods, type=type, trigger_field=trigger_field, required_fields=required_fields)
    routes.append(route)