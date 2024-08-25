from fastapi import FastAPI

from Registration.com.services.UserServices import UserServices

app = FastAPI()

add_controller = UserServices()


class UserController:
    @staticmethod
    @app.post("/insert user")
    def insert_user(UserName, password):
        try:
            add_controller.insert_user(UserName, password)
            return "User inserted"
        except Exception:
            return "Error"

    @app.get("/user")
    def get_user(UserId):
        try:
            add_controller.get_user(UserId)
            return "Success"
        except Exception:
            return "error"

    @app.delete("/{userid}/")
    def delete_user(UserId):
        try:
            add_controller.delete_user(UserId)
            return "address deleted"
        except Exception:
            return "address not deleted"

    @app.get("/{all_user}")
    def get_all_users(self):
        try:
            add_controller.get_all_users()
            return "ALL USERS"
        except Exception as e:
            return "ERROR"

