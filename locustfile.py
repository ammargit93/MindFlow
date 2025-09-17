from locust import HttpUser, task, between

class MindFlowUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def query_router(self):
        self.client.get("/mindflow/api/", params={"query": "tell me about the president"})
