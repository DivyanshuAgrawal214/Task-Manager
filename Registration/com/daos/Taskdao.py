from Registration.com.dbas.dbconnection import DBConnectivity
from sqlalchemy import text
from datetime import datetime


class TaskDao:
    def __init__(self):
        self.db_conn = DBConnectivity()
        self.engine, self.SessionLocal = self.db_conn.get_database_engine_and_session()

    def insert_tasks(self, title, description, status, priority, due_date, UserId):
        if not self.engine or not self.SessionLocal:
            print("Error: Could not establish database connection.")
            return

        session = self.SessionLocal()
        try:

            query = text("""
                        INSERT INTO tasks (title, description, status, priority, due_date, created_at, update_at, UserId)
                        VALUES (:title, :description, :status, :priority, :due_date, :created_at, :update_at, :UserId)
                        """)

            current_datetime = datetime.now()
            if isinstance(due_date, tuple):
                due_date = datetime(*due_date)

            session.execute(query, {
                'title': title,
                'description': description,
                'status': status,
                'priority': priority,
                'due_date': due_date,
                'created_at': current_datetime,
                'update_at': current_datetime,
                'UserId': UserId
            })

            session.commit()
            print("Task inserted successfully.")

        except Exception as e:
            session.rollback()
            print(f"Error inserting task: {e}")

    def read_task(self, task_id):

        if not self.engine or not self.SessionLocal:
            print("Error: Could not establish database connection.")
            return None

        session = self.SessionLocal()
        try:

            query = text("SELECT * FROM tasks WHERE TaskId = :task_id")

            result = session.execute(query, {'task_id': task_id})

            task = result.fetchone()

            if task:
                print("Task found:")
                print(task)
                return task
            else:
                print("Task not found.")
                return None

        except Exception as e:
            print(f"Error retrieving task: {e}")
            return None

    def update_task(self, task_id, title=None, description=None, status=None, priority=None, due_date=None):
        if not self.engine or not self.SessionLocal:
            print("Error: Could not establish database connection.")
            return

        session = self.SessionLocal()

        try:

            update_at = datetime.now()

            query = text("""
                UPDATE tasks
                SET title = COALESCE(:title, title),
                    description = COALESCE(:description, description),
                    status = COALESCE(:status, status),
                    priority = COALESCE(:priority, priority),
                    due_date = COALESCE(:due_date, due_date),
                    update_at = :update_at
                WHERE TaskId = :task_id
            """)

            if isinstance(due_date, tuple):
                due_date = datetime(*due_date)

            session.execute(query, {
                'task_id': task_id,
                'title': title,
                'description': description,
                'status': status,
                'priority': priority,
                'due_date': due_date,
                'update_at': update_at
            })

            session.commit()
            print("Task updated successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error updating task: {e}")

    def delete_task(self, task_id):
        if not self.engine or not self.SessionLocal:
            print("Error: Could not establish database connection.")
            return

        session = self.SessionLocal()

        try:

            check_query = text("SELECT COUNT(*) FROM tasks WHERE TaskId = :task_id")
            result = session.execute(check_query, {'task_id': task_id})
            count = result.scalar()  # Get the count of rows with the given TaskId

            if count == 0:
                print("Task not found.")
                return

            delete_query = text("DELETE FROM tasks WHERE TaskId = :task_id")

            session.execute(delete_query, {'task_id': task_id})

            session.commit()
            print("Task deleted successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting task: {e}")
