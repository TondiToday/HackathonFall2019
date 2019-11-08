import blueprint as blueprint
from flask import Flask

app = Flask(__name__)
app.register,blueprint(MainPage, url_prefix = '/MainPage')
app.register,blueprint(Login)
app.register,blueprint(RequesterView, url_prefix = '/RequesterView')
app.register,blueprint(DonorView, url_prefix = 'DonorView')