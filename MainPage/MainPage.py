from flask import Flask, Blueprint, render_template, request, redirect





app = Flask(__name__)
MainPage = Blueprint('MainPage',__name__, template_folder='/templates')



@MainPage.route('/')
def render_form():
    print('it worked')
    return render_template('MainPage.html')


@MainPage.route('/', methods=['POST'])
def login():
    if request.form == 'DonorLogin':
        print('it worked')
        return render_template('Login.html')

@MainPage.route('/', methods=['POST'])
def register():
    print('it worked')
    return render_template('/Login')