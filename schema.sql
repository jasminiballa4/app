CREATE TABLE sessions (
    id UUID PRIMARY KEY,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    duration INTEGER,
    summary TEXT
);

CREATE TABLE events (
    id TEXT PRIMARY KEY,
    session_id UUID REFERENCES sessions(id),
    event_type TEXT,
    content TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
