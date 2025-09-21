from huggingface_hub import InferenceClient
import os

class BackendClient:
    def __init__(self, model_type, api_url, inference_provider, model_id):
        self.model_type = model_type
        self.model_id = model_id
        self.api_url = api_url
        self.inference_provider = inference_provider
        
    def invoke(self, model_type):
        pass        



# API Inference client
class HFChatCompletionClient(BackendClient):
    def __init__(self, model_card, inference_provider, api_url):
        self.model_card = model_card
        self.inference_provider = inference_provider
        self.api_url = api_url
        self.client = InferenceClient(provider=self.inference_provider, api_key=os.getenv('HF_TOKEN'))

        
    def invoke(self, query):
        completion = self.client.chat.completions.create(
            model=self.model_card,
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ],
        )
        return completion.choices[0].message


