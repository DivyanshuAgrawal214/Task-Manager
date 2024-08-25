from fastapi import FastAPI
from Registration.com.services.FilterService import FilterService

app = FastAPI()

app_controller = FilterService()


class FilterController:
    @staticmethod
    @app.get("/tasks")
    def get_desired_task(status=None, priority=None, due_date=None):
        try:
            app_controller.get_desired_task(status, priority, due_date)
            return "SUCCESS"
        except Exception:
            return "Error"