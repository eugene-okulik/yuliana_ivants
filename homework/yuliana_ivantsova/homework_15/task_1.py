import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Добавляем студента
query_add_student = '''
INSERT INTO students (name, second_name)
VALUES (%s, %s)
'''
value = ("Yulli", "Ivantsova")

cursor.execute(query_add_student, value)
student_id = cursor.lastrowid

# Добавляем книги
query_add_book = '''
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
'''
value_books = [
    ('Капля духов в открытую рану', student_id),
    ('Подросток', student_id),
    ('Ученик убийцы', student_id)
]
cursor.executemany(query_add_book, value_books)

# Добавляем группу
query_add_group = '''
INSERT INTO `groups` (title, start_date, end_date)
VALUES ('AQA and Lit', '01.01.2026', '01.05.2027')
'''
cursor.execute(query_add_group)
group_id = cursor.lastrowid

# Добавляем студенту группу
query_update_student = '''
UPDATE students SET group_id = %s WHERE id = %s
'''
values_query = (group_id, student_id)
cursor.execute(query_update_student, values_query)

# Добавляем предметы
query_add_subjects = '''
INSERT INTO subjects (title)
VALUES (%s)
'''
subjects = ['literature', 'pythonx2']
subjects_ids = {}
for subject in subjects:
    cursor.execute(query_add_subjects, (subject,))
    subjects_id = cursor.lastrowid
    subjects_ids[subject] = subjects_id

# Добавляем уроки
query_add_lesson = '''
INSERT INTO lessons (title, subject_id) VALUES (%s, %s)
'''
lessons = [
    ('literature_begin', subjects_ids['literature']),
    ('literature_profi', subjects_ids['literature']),
    ('pythonx2 begin', subjects_ids['pythonx2']),
    ('pythonx2 profi', subjects_ids['pythonx2'])
]
lesson_ids = []
for title, subjects_id in lessons:
    cursor.execute(query_add_lesson, (title, subjects_id))
    lesson_ids.append(cursor.lastrowid)

# Добавляем оценки студента
query_mark_insert = '''
INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)
'''
value_mark = [
    (5, lesson_ids[0], student_id),
    (5, lesson_ids[1], student_id),
    (5, lesson_ids[2], student_id),
    (5, lesson_ids[3], student_id)
]
cursor.executemany(query_mark_insert, value_mark)

# Все оценки
query_mark_select = '''
SELECT value FROM marks WHERE student_id = %s
'''
cursor.execute(query_mark_select, (student_id,))
marks = cursor.fetchall()
print(marks)

# Все книги, которые находятся у студента
query_all_books = '''
SELECT title FROM books WHERE taken_by_student_id = %s
'''
cursor.execute(query_all_books, (student_id,))
books = cursor.fetchall()
print(books)

# Для вашего студента выведите всё
query_select_student = '''
SELECT
s.name,
s.second_name,
g.title AS group_name,
b.title AS book_title,
l.title AS lesson_title,
sub.title AS subject_title,
m.value AS mark
FROM students s
JOIN `groups` g on s.group_id = g.id
JOIN  books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = %s
'''
cursor.execute(query_select_student, (student_id,))
info_student = cursor.fetchall()
print(info_student)

db.commit()
db.close()
