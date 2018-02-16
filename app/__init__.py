from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Illionaire AOMG'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'mailtrap_username'
app.config['MAIL_PASSWORD'] = 'mailtrap_pword'


mail = Mail(app)
from app import views