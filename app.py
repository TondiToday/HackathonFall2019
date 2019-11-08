import blueprint as blueprint
from flask import Flask

app = Flask(__name__)
app.register,blueprint(MainPage)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
