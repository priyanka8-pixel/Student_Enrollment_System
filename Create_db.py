import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)

cur = conn.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS student_db")

print("✅ Database created successfully")

conn.close()


import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_db"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    father_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    clas VARCHAR(20),
    enrollment_date DATE
)
""")

print("✅ Table created successfully")

conn.close()
