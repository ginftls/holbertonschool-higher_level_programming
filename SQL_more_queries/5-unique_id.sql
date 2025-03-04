-- Creates the table unique_id with a unique id (default 1) and name
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
