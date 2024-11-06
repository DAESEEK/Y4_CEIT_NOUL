import psycopg2

# PostgreSQL 서버에 연결
connection = psycopg2.connect(
    host="localhost",
    database="daeseekpaek",
    user="daeseekpaek",
    password=""
)

# 커서 생성 및 쿼리 실행
cursor = connection.cursor()
cursor.execute("SELECT version();")
version = cursor.fetchone()
print("PostgreSQL version:", version)

# 연결 종료
cursor.close()
connection.close()
