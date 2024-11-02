import mysql.connector

# 데이터베이스 연결
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)
cursor = conn.cursor()

# 테이블 생성 예제
cursor.execute("""
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")

# 데이터 삽입 예제
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))
conn.commit()

# 데이터 조회 예제
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()