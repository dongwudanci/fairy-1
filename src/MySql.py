# 数据库处理库
from pymysql import *


class DB:
    def __init__(self):
        self.Table: str = NULL
        self.Field: str = '*'
        self.Where: str = '1 = 1'
        self.Order: str = NULL
        self.db = connect(host='127.0.0.1', user='drizzle', password='20011205', db='fairy')
        self.cursor = self.db.cursor(cursors.DictCursor)

    def table(self, table: str):
        self.Table = table
        return self

    def field(self, field: str):
        self.Field = field
        return self

    def where(self, where: str):
        self.Where = where
        return self

    def order(self, order: str):
        self.Order = order
        return self

    def item(self):
        sql = "SELECT %s FROM %s WHERE %s LIMIT 1" % (self.Field, self.Table, self.Where)
        if self.Order is not NULL:
            sql += " ORDER BY %s" % self.Order
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def list(self, num: int = NULL):
        sql = "SELECT %s FROM %s WHERE %s" % (self.Field, self.Table, self.Where)
        if num is not NULL:
            sql += " LIMIT %d" % num
        if self.Order is not NULL:
            sql += " ORDER BY %s" % self.Order
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert(self, **field):
        k, v = '', ''
        for key, value in field.items():
            k += key + ", "
            if isinstance(value, str):
                v += "'" + value + "', "
            else:
                v += value + ", "
        k = k[:-2]
        v = v[:-2]
        sql = "INSERT INTO %s(%s)VALUES (%s)" % (self.Table, k, v)
        self.cursor.execute(sql)
        return self.cursor.lastrowid
