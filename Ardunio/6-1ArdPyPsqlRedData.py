import psycopg2

# PostgreSQL 연결정
conn = psycopg2.connect(
    host="localhost",
    database="sensor_data",
    user="postgres",
    password=""  # 
)
cursor = conn.cursor()

# 데이터 읽기 함수
def read_data_from_postgresql():
    query = "SELECT * FROM sensor_values ORDER BY timestamp DESC;"
    cursor.execute(query)
    rows = cursor.fetchall()  # 모든 데이터를 가져옴

    # 결과 출력
    print("ID | Value | Timestamp")
    print("-" * 30)
    for row in rows:
        print(row)

# 함수 호출
read_data_from_postgresql()

# 연결 종료
cursor.close()
conn.close()