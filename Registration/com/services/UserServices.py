from Registration.com.daos.Userdao import Userdao


class UserServices:
    def __init__(self):
        self.add = Userdao()

    def insert_user(self, UserName, password):
        var = Userdao()
        return var.insert_user(UserName, password)

    def get_user(self, userid):
        var = Userdao()
        return var.get_user(userid)

    def delete_user(self, userid):
        var = Userdao()
        return var.delete_user(userid)
    def get_all_users(self):
        var = Userdao()
        return var.get_all_users()
