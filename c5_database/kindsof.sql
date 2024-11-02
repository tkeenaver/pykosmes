-- users 테이블 생성
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
-- orders 테이블 생성
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    product VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
-- 데이터 삽입
INSERT INTO users (id, name, email) 
    VALUES (1, 'Alice', 'alice@example.com');
INSERT INTO orders (order_id, user_id, product)
    VALUES (101, 1, 'Laptop');
-- 데이터 조회
SELECT u.name, o.product
    FROM users u
    JOIN orders o ON u.id = o.user_id;

-- MySQL 데이터베이스 생성 및 사용자 생성 예제
CREATE DATABASE example_db;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON example_db.* TO 'user'@'localhost';
FLUSH PRIVILEGES;
