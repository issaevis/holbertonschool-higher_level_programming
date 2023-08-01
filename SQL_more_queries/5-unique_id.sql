-- creates a table with unique id
CREATE TABLE IF NOT EXISTS unique_id(
    ID INTEGER DEFAULT 1 UNIQUE,
    name VARCHAR(256)
)