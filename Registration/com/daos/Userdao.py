from Registration.com.dbas.dbconnection import DBConnectivity
from sqlalchemy import text


class Userdao:
    def __init__(self):
        self.db_conn = DBConnectivity()
        self.engine, self.SessionLocal = self.db_conn.get_database_engine_and_session()

    def insert_user(self, UserName, password):
        if not self.engine or not self.SessionLocal:
            print("Error: Could not establish database connection.")
            return

        session = self.SessionLocal()

        try:
            query = text("INSERT INTO users (UserName, password) VALUES (:UserName, :password)")
            session.execute(query, {'UserName': UserName, 'password': password})
            session.commit()
            print("User inserted successfully.")
        except Exception as e:
            session.rollback()  # Rollback in case of error
            print(f"Error inserting user: {e}")

    def delete_user(self, id):
        session = self.SessionLocal()  # Create a new session
        try:
            query = text("DELETE FROM users WHERE UserId = :id")
            result = session.execute(query, {'id': id})
            if result.rowcount > 0:
                session.commit()
                print("User deleted successfully.")
            else:
                print("User not found.")
        except Exception as e:
            session.rollback()  # Rollback in case of error
            print(f"Error deleting user: {e}")

    def get_user(self, id):
        session = self.SessionLocal()  # Create a new session
        try:
            query = text("SELECT * FROM users WHERE UserId = :id")  # Ensure the placeholder matches the key
            result = session.execute(query, {'id': id})  # Corrected the parameter name to match the SQL placeholder
            user = result.fetchone()
            if user:
                return user
            else:
                print("User not found.")
                return None  # Explicitly return None if the user is not found
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None

    def get_all_users(self):
        session = self.SessionLocal()  # Create a new session
        try:
            query = text("SELECT * FROM users")
            result = session.execute(query)
            users = result.fetchall()
            return users
        except Exception as e:
            print(f"Error retrieving users: {e}")
