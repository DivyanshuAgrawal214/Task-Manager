from Registration.com.daos.SearchDao import SearchDao


class SearchService:
    def __init__(self):
        self.add = SearchDao()

    def search_tasks(self, title=None, description=None):
        var = SearchDao()
        return var.search_tasks(title,description)
