from fastapi import FastAPI
from Registration.com.services.TaskServices import TaskServices

app = FastAPI()

add_controller = TaskServices()


class TaskController:
    @staticmethod
    @app.post("/create task")
    def insert_tasks(title, description, status, priority, due_date, UserId):
        try:
            add_controller.insert_tasks(title, description, status, priority, due_date, UserId)
            return "User inserted"
        except Exception:
            return "Error"

    @app.get("/Task")
    def read_task(Taskid):
        try:
            add_controller.read_task(Taskid)
            return "Success"
        except Exception:
            return "error"
    @app.put("/Task")
    def update_task(task_id, title, description, status, priority, due_date=None):
        try:
            add_controller.update_task(task_id, title, description, status, priority, due_date=None)
            return "SUCCESS"
        except Exception:
            return "ERROR"

    @app.delete("/{Taskid}")
    def delete_task(task_id):
        try:
            add_controller.delete_task(task_id)
            return "SUCCESS"
        except Exception:
            return "ERROR"


