from flask import Flask
from flask import render_template
from config import Config

from app.routes.rUser import userBp


app = Flask(__name__)
app.secret_key = Config().SECRET_KEY

app.register_blueprint(userBp)


@app.route('/')
def index():
    return render_template("index.html", title="Zilong Home Page ")


@app.route('/status.json')
def statusjson():
    return '{"time_":"2017-01-02 21:16:53"}'


@app.route('/channelIos600')
def channelIos600():
    return render_template("channelIos600.html", title="channelIos600")


if __name__ == '__main__':
    # open debug model
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
