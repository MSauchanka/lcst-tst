from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):

    @task()
    def index(self):
        response = self.client.get("/batch/monitoring/jobs/executions/1")
        print("Response status code: {}".format(response.content))


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
