from MySql import *
from String import md5


class Account:
    def __init__(self):
        self.db: DB = DB()
        self.id: str = NULL
        self.password: str = NULL
        self.email: str = NULL

    def login(self, email, password):
        res = self.db.table('user').where("email = '%s' and password = '%s'" % (email, md5(password))).item()
        if res is None:
            return False
        else:
            return True