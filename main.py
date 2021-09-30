from project import create_app
#from project.dao.Dao import DAO

app = create_app()
#DAO = DAO(app)

if __name__ == "__main__":
    app.run(debug=True,port=5000)