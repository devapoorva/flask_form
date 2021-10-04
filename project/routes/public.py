from flask import Blueprint,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo
import sys
from project.forms.login import LoginForm
from project.utils.functions import *

# user_controller = UserController(Dao)

public_routes = Blueprint('public_routes',__name__,template_folder="/templates")

from project.controllers.UserController import UserController

@public_routes.route('/',methods=['GET','POST'])
def home():
    login = LoginForm()
    if login.validate_on_submit():
        print(login.name.data, file=sys.stderr)

    return render_template("index.html",form=login)

@public_routes.route('/register',methods=['POST'])
def register():
    from project import mysql
    login = LoginForm()
    if login.validate_on_submit():
        print(login.username.data, file=sys.stderr)
        userController = UserController()
        return userController.addUser(login.username.data,login.email.data,hash(login.password.data),"12345")
        
    else:
        return render_template("index.html",form=login)

