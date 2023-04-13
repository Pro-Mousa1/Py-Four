from peewee import *
from os import path
db_connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(db_connection, "eMobilis.db"))

# Create a table for users


class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)


class Product(Model):
    name = CharField()
    quantity = CharField()
    price = CharField()

    class Meta:
        database = db


Product.create_table(fail_silently=True)


class Employee(Model):
    name = CharField()
    badge_no = IntegerField()
    work_field = CharField()

    class Meta:
        database = db


Employee.create_table(fail_silently=True)


class Admin(Model):
    name = CharField()
    email = CharField()
    agenda = CharField()
    account = CharField()
    location = CharField()

    class Meta:
        database = db


Admin.create_table(fail_silently=True)
