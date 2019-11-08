import blueprint as blueprint
from flask import Flask

app = Flask(__name__)
app.register,blueprint(MainPage)
app.register,blueprint(Login)
app.register,blueprint(RequesterView)
app.register,blueprint(DonorView)