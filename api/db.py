# from psycopg2 import pool
import psycopg2
import os
from urllib.parse import urlparse

result = urlparse(os.environ.get('DATABASE_URL'))
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname



def connect():
    return psycopg2.connect(user=username, password=password, database=database, host=hostname)
