import sqlite3

DATABASE_NAME = "botnews.db"

def get_connection():
    return sqlite3.connect(DATABASE_NAME)
