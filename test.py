from src.MySql import *
from src.String import md5

db = DB()
res = db.table('user').where(" email = 'i1@drizzle.vip' ").item()

