__author__ = 'Elf'

from peewee import *
import datetime
virastar_db = MySQLDatabase('virastar_db', host='127.0.0.1', user='root', passwd='')


class BaseModel(Model):
    class Meta:
        database = virastar_db


class Users(BaseModel):
    id = PrimaryKeyField()
    email = CharField()
    token = IntegerField()
    status = IntegerField()
    date = DateField(default=datetime.datetime.now().date())

