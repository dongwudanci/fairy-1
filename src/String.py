# 字符串处理库
import hashlib
import jwt


def md5(string: str):
    res = hashlib.md5()
    res.update(string.encode('utf-8'))
    return res.hexdigest()