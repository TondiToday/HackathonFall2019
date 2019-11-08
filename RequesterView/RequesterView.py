from flask import Flask, Blueprint





app = Flask(__name__)
MainPage = Blueprint('RequesterView',__name__, template_folder='/templates')



@RequesterView.route('/')



@RequesterView.route('/', methods=['POST'])