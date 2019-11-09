from flask import Flask, Blueprint, render_template





app = Flask(__name__)
Login = Blueprint('Login',__name__, template_folder='/templates')



@Login.route('/')
def render_form():
    return render_template('Login.html')


#@Login.route('/', methods=['POST'])
