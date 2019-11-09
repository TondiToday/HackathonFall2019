from flask import Flask, Blueprint





app = Flask(__name__)
MainPage = Blueprint('DonorView',__name__, template_folder='/templates')



#@DonorView.route('/')



#@DonorView.route('/', methods=['POST'])