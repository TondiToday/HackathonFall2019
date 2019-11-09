from flask import Blueprint, render_template

main = Blueprint('auth', __name__)

@auth.route('/login'):
def login():
    return render_template('Login.html')

#@auth.route('/login', methods = ['POST'])
#def login_post():

@auth.route('/signup')
def signup():
    render_template('signup.html')

#auth.route('/signup', methods = ['POST'])
#def signup_post():

@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))