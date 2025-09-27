class Route:
    def __init__(self, route_name, urls, methods, type, trigger_field,required_fields):
        self.required_fields = required_fields
        self.trigger_field = trigger_field
        self.route_name = route_name
        self.methods = methods
        self.type = type
        self.urls = urls
    
    
        
        
        
        
    