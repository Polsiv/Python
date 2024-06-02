CREATE TABLE IF NOT EXISTS numbers (
    num INTEGER PRIMARY KEY, 
    num_evaluated TEXT,
    active BOOLEAN
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    public_id TEXT(20) UNIQUE,
    username TEXT NOT NULL UNIQUE,
    u_password TEXT NOT NULL
);
