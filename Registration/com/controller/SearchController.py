from fastapi import FastAPI
from Registration.com.services.SearchService import SearchService

app = FastAPI()

app_controller = SearchService()


class SearchController:
    @staticmethod
    @app.get("/Search")
    def search_tasks(title=None, description=None):
        try:
            app_controller.search_tasks(title, description)
            return "SUCCESS"
        except Exception:
            return "Error"
