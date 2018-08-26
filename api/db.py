# from psycopg2 import pool
import psycopg2
import os

user = os.environ.get('DATABASE_USER') or 'postgres'
password = os.environ.get('DATABASE_PASSWORD') or 'xbt3ybot9'
database = os.environ.get('DATABASE_NAME') or 'stackoverflowliteapi'
host = os.environ.get('DATABASE_URL') or 'localhost'


def connect():
    return psycopg2.connect(user=user, password=password, database=database, host=host)
