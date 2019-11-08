from flask import Flask, Blueprint





app = Flask(__name__)
MainPage = Blueprint('DonorView',__name__, template_folder='/templates')



@main_page.route('/')



@main_page.route('/', methods=['POST'])