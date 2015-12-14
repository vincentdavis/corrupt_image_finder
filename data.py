from peewee import *
import datetime

#db = SqliteDatabase('GrandCounty.db')
db = MySQLDatabase('GrandCounty', user='scraper')


class BaseModel(Model):
    class Meta:
        database = db

class Images(BaseModel):
    FullPath = CharField(unique=True)
    Path = CharField()
    File_Name = CharField()
    Exif_Test = Bool()
    Pil_Test = Bool()
    Timestamp = DateTimeField(default=datetime.datetime.now)