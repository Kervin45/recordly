from models import Record
import datetime

def create_record(conn, title, content, tags=None):
    sql = """INSERT INTO records (title, content, tags, created_at, updated_at)
             VALUES (?, ?, ?, ?, ?)"""
    now = datetime.datetime.now().isoformat()
    cur = conn.cursor()
    cur.execute(sql, (title, content, tags, now, now))
    conn.commit()
    return Record(cur.lastrowid, title, content, tags, now, now)


def get_record(conn, record_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM records WHERE id = ?", (record_id,))
    row = cur.fetchone()
    return Record.from_row(row) if row else None

def get_all_records(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM records")
    return [Record.from_row(row) for row in cur.fetchall()]


def update_record(conn, record_id, title, content, tags):
    sql = """UPDATE records 
             SET title=?, content=?, tags=?, updated_at=? 
             WHERE id=?"""
    now = datetime.datetime.now().isoformat()
    cur = conn.cursor()
    cur.execute(sql, (title, content, tags, now, record_id))
    conn.commit()
    return cur.rowcount > 0


def delete_record(conn, record_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM records WHERE id=?", (record_id,))
    conn.commit()
    return cur.rowcount > 0


