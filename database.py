import sqlite3


DB_NAME = "recordly.db"


def create_connection(db_name=DB_NAME):
    return sqlite3.connect(db_name)


def create_tables(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT,
            created_at TEXT,
            updated_at TEXT
        )
    """)
    conn.commit()
