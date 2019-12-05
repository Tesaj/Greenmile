from flask_login import UserMixin
from greenmile import app,login,db
from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy import event

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model ,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(80),unique=False,nullable=False)
    

    def check_password(self,password):
        return check_password_hash(self.password,password)


    def __repr__(self):
        return '<User %r>' % self.username

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    company =db.Column(db.String(180), unique=True, nullable=False)

    def __repr__(self):
        return '<Supplier %r>' % self.supplier

class Loader(db.Model):
    __tablename__ = 'loader'
    id = db.Column(db.Integer, primary_key=True)
    loader = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Loader %r>' % self.loader

class Packages(db.Model):
    __tablename__ = 'Packages'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(1000), unique=True, nullable=False)
    Category = db.Column(db.String(1000), unique=True, nullable=False)
    Quantity = db.Column(db.Integer,primary_key=True)
    Unit = db.Column(db.Integer,primary_key=True)
    Price = db.Column(db.Integer,primary_key=True)
    

    def __repr__(self):
        return '<Packages %r>' % self.packages

class Recipitent(db.Model):
    __tablename__ = 'Recipitent'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(1000), unique=True, nullable=False)
    Goods = db.Column(db.String(1000), unique=True, nullable=False)
    

    def __repr__(self):
        return '<Recipitent %r>' % self.recipitent

@event.listens_for(User.password,'set',retval=True)
def hash_user_password(target,value,oldvalue,initiator):
    if value != oldvalue:
        return generate_password_hash(value).decode("utf-8")
    return value 


