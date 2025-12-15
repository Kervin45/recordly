from flask import Flask, render_template, request, redirect
from database import create_connection, create_tables
from crud import (
    create_record,
    get_all_records,
    get_record,
    update_record,
    delete_record
)

app = Flask(__name__)

# init DB once
conn = create_connection()
create_tables(conn)
conn.close()

@app.route("/")
def index():
    conn = create_connection()
    records = get_all_records(conn)
    conn.close()
    return render_template("index.html", records=records)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        conn = create_connection()
        create_record(
            conn,
            request.form["title"],
            request.form["content"],
            request.form.get("tags")
        )
        conn.close()
        return redirect("/")
    return render_template("form.html", action="Create")

@app.route("/edit/<int:record_id>", methods=["GET", "POST"])
def edit(record_id):
    conn = create_connection()
    record = get_record(conn, record_id)

    if request.method == "POST":
        update_record(
            conn,
            record_id,
            request.form["title"],
            request.form["content"],
            request.form.get("tags")
        )
        conn.close()
        return redirect("/")

    conn.close()
    return render_template("form.html", action="Edit", record=record)

@app.route("/delete/<int:record_id>")
def delete(record_id):
    conn = create_connection()
    delete_record(conn, record_id)
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
