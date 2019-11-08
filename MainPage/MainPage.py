from flask import Flask, Blueprint





app = Flask(__name__)
MainPage = Blueprint('MainPage',__name__, template_folder='/templates')
