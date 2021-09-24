from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "flask form "

    from project.routes.public import public_routes
    from project.routes.user import user_routes

    app.register_blueprint(public_routes,url_prefix="/")
    app.register_blueprint(user_routes,url_prefix="/user")
    return app

