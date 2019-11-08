from flask import Flask, Blueprint





app = Flask(__name__)
MainPage = Blueprint('Login',__name__, template_folder='/templates')



@login.route('/')



@login.route('/', methods=['POST'])