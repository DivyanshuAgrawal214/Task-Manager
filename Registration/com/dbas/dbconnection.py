from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectivity:
    def get_database_engine_and_session(self, username="Your_username", password="your_password", hostname="your_host", port="portno.",
                                        database="Ur_database"):
        try:

            DATABASE = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}"
            engine = create_engine(DATABASE)

            # Create session factory
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

            print("Database engine and session factory created successfully.")
            return engine, SessionLocal
        except Exception as e:
            print(f"Error creating database engine and session: {e}")
            return None
