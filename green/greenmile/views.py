from flask import render_template,redirect,url_for,flash,request,abort
from greenmile.models import Loader,Supplier,User,Packages,Recipitent
from greenmile import app,db
from flask_admin import Admin,AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager,current_user,login_user,logout_user
from greenmile.forms import LoginForm

@app.route('/login', methods=['POST', 'GET'])
def home():
    if current_user.is_authenticated:
        return redirect('admin')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        elif(user.role == 'Admin'):
            login_user(user)
            return redirect('admin')
        elif(user.role == 'Supplier'):
            login_user(user)
            return redirect(url_for('userhome'))
        elif(user.role == 'Loader'):
            login_user(user)
            return redirect(url_for('userhome'))
        else:
            login_user(user)
            flash('sorry! You need to be an admin')
            return redirect('admin')
    # return render_template('login.html', title='Sign In', form=form)


    return render_template('index.html',form=form)


@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/',methods=['POST','GET'])
def userhome():
    return render_template('home.html')





@app.route('/logout')
def logout():
    logout_user()
    return 'Logged Out'     






class UserModelView(ModelView):
    form_choices ={
        'role':[
        ('Admin','Admin'),
        ('Supplier','Supplier'),
        ('Loader','Loader'),
        ('Recipitent','Recipitent'),
        ('Packages','Packages')
        ]
    }

    # def is_accessible(self):
    #     return current_user.is_authenticated

    # def inaccessible_callback(self,name,**kwargs):
    #     return redirect(url_for('login')) 
    
class MyAdminIndexView(AdminIndexView):
    # def is_accessible(self):
    #     return current_user.is_authenticated

    pass



admin = Admin(app, name='greenmile', template_mode='bootstrap3',index_view=MyAdminIndexView())
admin.add_view(UserModelView(User,db.session))
admin.add_view(UserModelView(Supplier, db.session))
admin.add_view(UserModelView(Loader, db.session))
admin.add_view(UserModelView(Packages, db.session))
admin.add_view(UserModelView(Recipitent, db.session))


