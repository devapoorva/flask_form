from flask import Blueprint,render_template

user_routes = Blueprint('user_routes',__name__,template_folder="/templates")

@user_routes.route('/')
def user_dashboard():
    return render_template("user_dashboard.html")