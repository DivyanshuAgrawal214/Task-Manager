from fastapi import HTTPException
from Registration.com.dbas.dbconnection import DBConnectivity
from sqlalchemy import text



class FilterDao:
    def __init__(self):
        self.db_conn = DBConnectivity()
        self.engine, self.SessionLocal = self.db_conn.get_database_engine_and_session()

    def get_desired_task(self, status=None, priority=None, due_date=None):
        if not self.engine or not self.SessionLocal:
            print("Error: Could not establish database connection.")
            return

        session = self.SessionLocal()
        try:
            query = "SELECT * FROM tasks WHERE 1=1"
            params = {}
            if status:
                query += " AND status = :status"
                params['status'] = status
            if priority is not None:
                query += " AND priority = :priority"
                params['priority'] = priority
            if due_date:
                query += " AND due_date = :due_date"
                params['due_date'] = due_date
            result = session.execute(text(query), params)
            tasks = result.fetchall()

            if not tasks:
                raise HTTPException(status_code=404, detail="No tasks found with the specified filters.")

            return [dict(task) for task in tasks]

        except Exception as e:
            print(f"Error filtering tasks: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
