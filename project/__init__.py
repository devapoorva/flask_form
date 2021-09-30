from flask import Flask


def create_app():
    app = Flask(__name__)
    
    from project.routes.public import public_routes
    from project.routes.user import user_routes
    app.config['SECRET_KEY'] = "526a563062e3adbd75bd8c64c3a33675"
    app.register_blueprint(public_routes,url_prefix="/")
    app.register_blueprint(user_routes,url_prefix="/user")
    return app

