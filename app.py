from flask import Flask, render_template

app = Flask(__name__)


# 游戏主页
@app.route('/')
def index():  # put application's code here
    return render_template('main.html')


# 公告
@app.route('/notice')
def notice():
    return render_template('notice.html')


if __name__ == '__main__':
    app.run()
