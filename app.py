from flask import Flask, request, render_template, redirect, jsonify
from database import create_connection, create_tables
from crud import (
    create_record,
    get_record,
    get_all_records,
    update_record,
    delete_record
)

app = Flask(__name__)

# -----------------------------
# Database initialization
# -----------------------------
def get_db():
    return create_connection()

with get_db() as conn:
    create_tables(conn)

# -----------------------------
# UI ROUTES
# -----------------------------

@app.route("/", methods=["GET"])
def home():
    conn = get_db()
    records = get_all_records(conn)
    conn.close()
    return render_template("index.html", records=records)


@app.route("/records", methods=["POST"])
def add_record():
    data = request.form
    conn = get_db()
    create_record(
        conn,
        data["title"],
        data["content"],
        data.get("tags")
    )
    conn.close()
    return redirect("/")


# -----------------------------
# API ROUTES (for learning / future)
# -----------------------------

@app.route("/api/records", methods=["GET"])
def api_get_all():
    conn = get_db()
    records = get_all_records(conn)
    conn.close()
    return jsonify([r.to_dict() for r in records])


@app.route("/api/records/<int:record_id>", methods=["GET"])
def api_get_one(record_id):
    conn = get_db()
    record = get_record(conn, record_id)
    conn.close()
    if not record:
        return jsonify({"error": "Not found"}), 404
    return jsonify(record.to_dict())


@app.route("/api/records", methods=["POST"])
def api_create():
    data = request.json
    conn = get_db()
    record = create_record(
        conn,
        data["title"],
        data["content"],
        data.get("tags")
    )
    conn.close()
    return jsonify(record.to_dict()), 201


@app.route("/api/records/<int:record_id>", methods=["PUT"])
def api_update(record_id):
    data = request.json
    conn = get_db()
    success = update_record(
        conn,
        record_id,
        data["title"],
        data["content"],
        data.get("tags")
    )
    conn.close()
    return jsonify({"updated": success})


@app.route("/api/records/<int:record_id>", methods=["DELETE"])
def api_delete(record_id):
    conn = get_db()
    success = delete_record(conn, record_id)
    conn.close()
    return jsonify({"deleted": success})


if __name__ == "__main__":
    app.run(debug=True)
