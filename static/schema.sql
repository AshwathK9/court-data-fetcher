-- schema.sql
CREATE TABLE IF NOT EXISTS queries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_type TEXT,
    case_number TEXT,
    year TEXT,
    html TEXT,
    parsed_json TEXT,
    created_at TEXT
);
