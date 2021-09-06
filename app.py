from flask import Flask, render_template, make_response, request, redirect
from src.String import *

app = Flask(__name__)


# 游戏主页
@app.route('/')
def index():  # put application's code here
    token = request.cookies.get('token')
    if token is not None:
        return render_template('main.html')
    else:
        return redirect('/login')


# 登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        from src.Account import Account
        account = Account()
        res = account.login(request.form.get('email'), request.form.get('password'))
        if not res:
            return '登录失败'
        else:
            r = make_response(redirect('/'))
            r.set_cookie('token', res)
            return r


# 公告
@app.route('/notice')
def notice():
    return render_template('notice.html')


@app.route('/test')
def test():
    r = make_response()
    r.set_cookie('token', '233')
    return r


if __name__ == '__main__':
    app.run()
