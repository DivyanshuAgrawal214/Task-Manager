from Registration.com.dbas.dbconnection import DBConnectivity
from sqlalchemy import text


class SearchDao:
    def __init__(self):
        self.db_conn = DBConnectivity()
        self.engine, self.SessionLocal = self.db_conn.get_database_engine_and_session()

    def search_tasks(self, title=None, description=None):
        session = self.SessionLocal()

        try:
            base_query = "SELECT * FROM tasks WHERE"
            conditions = []
            params = {}

            if title:
                conditions.append("title LIKE :title")
                params['title'] = f"%{title}%"
            if description:
                conditions.append("description LIKE :description")
                params['description'] = f"%{description}%"

            if conditions:
                final_query = f"{base_query} {' OR '.join(conditions)}"
            else:
                final_query = "SELECT * FROM tasks"

            query = text(final_query)
            result = session.execute(query, params)
            tasks = result.fetchall()

            return tasks

        except Exception as e:
            print(f"Error searching tasks: {e}")
            return []
