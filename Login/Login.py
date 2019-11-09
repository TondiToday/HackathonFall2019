from flask import Flask, Blueprint, render_template, request
from flask import Flask, Blueprint
import json
import os
import sqlite3

from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests
from db import init_db_command
from user import User
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"




app = Flask(__name__)
Login = Blueprint('Login',__name__, template_folder='/templates')



@Login.route('/')
def Donor_Login():
    return render_template('/Login.html')


@Login.route('/', methods=['POST'])
def Donor():
    return render_template('profile.html')