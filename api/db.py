# from psycopg2 import pool
import psycopg2
import os


def connect():
    return psycopg2.connect(user="postgres", password="admin16345", database="stackoverflowliteapi", host="localhost")
