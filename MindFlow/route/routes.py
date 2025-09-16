class Route:
    def __init__(self, route_name, model_card, inference_provider, api_url):
        self.route_name = route_name
        self.model_card = model_card
        self.inference_provider = inference_provider
        self.api_url = api_url
        
    