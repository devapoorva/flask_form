from project.dao.DAO import DAO
from project.Database.DB import DB

class DBDAO(DB):
    def __init__(self, app):
        super(DBDAO, self).__init__(app)
    