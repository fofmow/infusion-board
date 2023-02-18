from os import environ

from peewee import PostgresqlDatabase
from pytz import timezone

database = PostgresqlDatabase(
    environ.get("DB_NAME"),
    user=environ.get("DB_USER"),
    password=environ.get("DB_PASSWORD"),
    host=environ.get("DB_HOST"),
    port=environ.get("DB_PORT")
)

MOSCOW_TZ = timezone("Europe/Moscow")

DT_FORMAT = "%Y-%m-%d %H:%M:%S"
