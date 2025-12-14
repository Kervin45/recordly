# Recordly

A Flask-based REST API for managing records.

## Project Structure

```
recordly/
├── app.py              # Main Flask application
├── database.py         # Database configuration
├── models.py           # SQLAlchemy models
├── routes/             # Route handlers
│   └── records.py      # Record endpoints
├── schemas.py          # Marshmallow schemas
├── utils/              # Utility functions
└── README.md           # This file
```

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy marshmallow
   ```

## Running the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

- `GET /api/records` - Get all records
- `GET /api/records/<id>` - Get a specific record
- `POST /api/records` - Create a new record
- `PUT /api/records/<id>` - Update a record
- `DELETE /api/records/<id>` - Delete a record

## License

MIT
