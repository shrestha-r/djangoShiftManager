import psycopg2

try:
    conn = psycopg2.connect(
        host="agencymanager.cf44guwymji8.eu-north-1.rds.amazonaws.com",
        database="agencymanager",
        user="postgres",
        password="g4#G00gle",
        port=5432
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)

