from locust import HttpUser, task, between


class LoadTestUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_index(self):
        self.client.get("/ping")
