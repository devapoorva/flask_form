from flask_mysqldb import MySQL

class DB(object):
    def __init__(self, app):
        app.config['SECRET_KEY'] = "edfc73cb53371e8e0d5cf6996fe0481f"
        app.config['MYSQL_HOST'] = "localhost"
        app.config['MYSQL_USER'] = "root"
        app.config["MYSQL_PASSWORD"] = ""
        app.config["MYSQL_DB"] = "flask_form"
        self.mysql = MySQL(app)
        
    def cur(self):
		return self.mysql.connection.cursor()
    
    def query(self, q):
		h = self.cur()
		if (len(self.table)>0):
			q = q.replace("@table", self.table)
		h.execute(q)
		return h
    
    def commit(self):
        self.mysql.connection.commit()
    