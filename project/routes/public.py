from flask import Blueprint,render_template

public_routes = Blueprint('public_routes',__name__,template_folder="/templates")

@public_routes.route('/')
def home():
    return render_template("index.html")