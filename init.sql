CREATE DATABASE IF NOT EXISTS clickops;
USE clickops;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    gender VARCHAR(10)
);

