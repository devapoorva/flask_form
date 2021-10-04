from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "526a563062e3adbd75bd8c64c3a33675"

from project.routes.public import public_routes
from project.routes.user import user_routes 
app.register_blueprint(public_routes,url_prefix="/")
app.register_blueprint(user_routes,url_prefix="/user")

from flask_mysqldb import MySQL
app.config['SECRET_KEY'] = "edfc73cb53371e8e0d5cf6996fe0481f"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask_form"
app.config["MYSQL_PORT"] = "3306"

mysql = MySQL(app)