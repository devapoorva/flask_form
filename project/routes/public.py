from flask import Blueprint,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo
import sys
from project.forms.login import LoginForm

public_routes = Blueprint('public_routes',__name__,template_folder="/templates")

@public_routes.route('/',methods=['GET','POST'])
def home():
    login = LoginForm()
    if login.validate_on_submit():
        print(login.name.data, file=sys.stderr)

    return render_template("index.html",form=login)

@public_routes.route('/register',methods=['POST'])
def register():
    login = LoginForm()
    if login.validate_on_submit():
        print(login.username.data, file=sys.stderr)
        return ''' 
        <h1>Form submitted successfully </h1>
        <h3>Email {} </h3>
        <h4>Password {} </h4>
        <h4>Username {} </h4>
          '''.format(login.email.data,login.password.data,login.username.data)
    else:
        return render_template("index.html",form=login)

