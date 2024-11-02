import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 테이블 생성 예제
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

# 데이터 삽입 예제
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
conn.commit()

# 데이터 조회 예제
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
