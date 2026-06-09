import sqlite3

def connect_database():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    return conn, cursor

def close_database():
    conn = sqlite3.connect('tasks.db')
    conn.close()

def create_table():
    conn, cursor = connect_database()
    cursor.execute("""
           CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   is_done INTEGER DEFAULT 0)
""")
    conn.commit()

create_table()
close_database()