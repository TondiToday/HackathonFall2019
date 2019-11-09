from flask import Flask, Blueprint, render_template





app = Flask(__name__)
Register = Blueprint('Register',__name__, template_folder='/templates')



@Register.route('/')
def render_form():
    return render_template('Register.html')
