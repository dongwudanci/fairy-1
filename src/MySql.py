from pymysql import *


class DB:
    def __init__(self):
        self.Table: str = NULL
        self.Field: str = NULL
        self.Where: str = NULL
        db = connect(host='127.0.0.1', user='drizzle', password='20011205', db='fairy')
        self.cursor = db.cursor()

    def table(self, table: str):
        self.Table = table

    def field(self, field: str):
        self.Field = field

    def where(self, where: str):
        self.Where = where

    def item(self):
        sql = "SELECT %s FROM %s WHERE %s LIMIT 1" % (self.Field, self.Table, self.Where)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def list(self, num: int = NULL):
        sql = "SELECT %s FROM %s WHERE %s" % (self.Field, self.Table, self.Where)
        if num is not NULL:
            sql += " LIMIT %d" % num
        self.cursor.execute(sql)
        return self.cursor.fetchall()
