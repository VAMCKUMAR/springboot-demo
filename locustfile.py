from locust import HttpUser, task, between

class SpringBootUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_endpoint(self):
        self.client.get("/hello")

    @task
    def cpu_endpoint(self):
        self.client.get("/cpu")
