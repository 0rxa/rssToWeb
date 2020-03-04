from peewee import *

db_name = 'earthquakedb'
db_user = 'root'
db_pw = 'my-secret-pw'
db_host = 'localhost'
db_port = 3306
db = MySQLDatabase(db_name,
        user=db_user,
        password=db_pw,
        host=db_host,
        port=db_port)

class earthquakes(Model):
    datetime = DateTimeField(db_column = "dtime")
    latitude = DoubleField(db_column = "latitude")
    longitude = DoubleField(db_column = "longitude")
    depth = DoubleField(db_column = "depth")
    position = CharField(db_column = "position") 
    magnitude = DoubleField(db_column = "magnitude")

    class Meta():
        database = db
