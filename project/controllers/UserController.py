from project.models.user import User
class UserController():

    def addUser(self,name,email,password,mobile):
        from project import mysql
        cursor = mysql.connection.cursor() 
        cursor.execute('''INSERT INTO users(name,email,password,mobile) VALUES(
            '{}','{}','{}','{}'
        )'''.format(name,email,password,mobile))
        mysql.connection.commit()
        user = User()
        user_info = {"name": name, "email": email, "password": password,"mobile":mobile}
        return str(user.allUsers)
        