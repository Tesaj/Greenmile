from flask import Flask, abort, flash, redirect,url_for
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_login import UserMixin
from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/green.db'
app.config['SECRET_KEY']='girls and boys'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    company =db.Column(db.String(180), unique=True, nullable=False)

    def __repr__(self):
        return '<Supplier %r>' % self.supplier

class Loader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loader = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Loader %r>' % self.loader


    


app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='myapp', template_mode='bootstrap3')
admin.add_view(ModelView(Supplier, db.session))
admin.add_view(ModelView(Loader, db.session))
admin.add_view(ModelView(User, db.session))




 
@app.route('/login', methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route('/adminlogin',methods=['POST','GET'])
def admin():
    return render_template('adminlogin.html')


@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/home',methods=['POST','GET'])
def userhome():
    return render_template('home.html')


login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(
        form.password.data):

            login_user(user)
        if user.is_admin:
            return redirect(url_for('127.0.0.1:5000/admin/'))    
        else:
            return redirect(url_for('http://127.0.0.1:5000/'))
    else:
        flash('Invalid username or password.')




if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=5000)
