import torndb
import MySQLdb

class BlogDb(object):
    def __init__(self, host, database, user, password):
        self._db = torndb.Connection(
                host=host, database=database,
                user=user, password=password)



