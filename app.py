from flask import Flask,Blueprint
#from DonorView.DonorView import DonorView
from Login.Login import Login
from Register.Register import Register
from MainPage.MainPage import MainPage
#from RequesterView.RequesterView import RequesterView

app = Flask(__name__)
app.register_blueprint(MainPage)
app.register_blueprint(Login, url_prefix = '/Login')
app.register_blueprint(Register, url_prefix = '/Register')
#app.register_blueprint(RequesterView, url_prefix = '/RequesterView')
#app.register_blueprint(DonorView, url_prefix = 'DonorView')

if __name__ == "__main__":
    app.run(Debug=True)