import csv
from pathlib import Path
import mysql.connector as mysql
import os
import dotenv


base_dir = Path(__file__).resolve().parents[2]
file_path = base_dir / 'eugene_okulik' / 'Lesson_16' / 'hw_data' / 'data.csv'

dotenv.load_dotenv()

db_connect = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db_connect.cursor(dictionary=True)

query_select_student = '''
        SELECT s.name, s.second_name,
        g.title AS group_name, b.title AS book_title,
        l.title AS lesson_title, sub.title AS subject_title,
        m.value AS mark
        FROM students s
        JOIN `groups` g on s.group_id = g.id
        JOIN  books b ON b.taken_by_student_id = s.id
        JOIN marks m ON m.student_id = s.id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjects sub ON l.subject_id = sub.id
'''
cursor.execute(query_select_student)
info_student = cursor.fetchall()

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        if row not in info_student:
            data.append(row)


print(row)

db_connect.close()
