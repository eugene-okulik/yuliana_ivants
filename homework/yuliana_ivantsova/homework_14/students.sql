INSERT INTO students (name, second_name)
SELECT 'Yuliana', 'Ivantsova'
WHERE NOT EXISTS (
SELECT *
FROM students 
WHERE name = 'Yuliana' AND second_name = 'Ivantsova'
)

SELECT * 
FROM students
WHERE name = 'Yuliana' AND second_name = 'Ivantsova'

UPDATE students s 
SET group_id = (
SELECT id
FROM `groups` g
WHERE title = 'AQA and literature' AND end_date = '01.05.2027'
)
WHERE name = 'Yuliana' AND second_name = 'Ivantsova'
