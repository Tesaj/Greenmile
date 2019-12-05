from flask import Flask, abort, flash, redirect,url_for
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager,current_user,login_user,logout_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///green.db'
app.config['SECRET_KEY']='mysecret'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
login = LoginManager(app)
login.init_app(app)




from greenmile import views

 


if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=5000)
