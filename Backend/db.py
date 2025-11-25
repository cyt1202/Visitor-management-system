import sqlite3
import os
from flask import g

'''
This file is to connect to the database
'''

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "visitor.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()