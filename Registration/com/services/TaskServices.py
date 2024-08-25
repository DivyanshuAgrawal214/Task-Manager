from Registration.com.daos.Taskdao import TaskDao


class TaskServices:
    def __init__(self):
        self.add = TaskDao()

    def insert_tasks(self, title, description, status, priority, due_date, UserId):
        var = TaskDao()
        return var.insert_tasks(title, description, status, priority, due_date, UserId)

    def read_task(self, task_id):
        var = TaskDao()
        return var.read_task(task_id)

    def update_task(self, task_id, title, description, status, priority, due_date=None):
        var = TaskDao()
        return var.update_task(task_id, title, description, status, priority, due_date)

    def delete_task(self, task_id):
        var = TaskDao()
        return var.delete_task(task_id)