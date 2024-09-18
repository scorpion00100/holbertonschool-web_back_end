-- Script that creates a table users
-- Create the table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL,
    PRIMARY KEY (id)
);
