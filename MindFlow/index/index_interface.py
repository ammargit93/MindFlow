from app.config import default_cfg

class IndexInterface:
    def __init__(self):
        self.embeddings = default_cfg['embeddings']
        self.vectordb = default_cfg['vectordb']
        
        
    