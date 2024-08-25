from Registration.com.daos.FilterDao import FilterDao

class FilterService:
    def __init__(self):
        self.add = FilterDao()

    def get_desired_task(self, status=None, priority=None, due_date=None):
        var = FilterDao()
        return var.get_desired_task(status, priority, due_date)


