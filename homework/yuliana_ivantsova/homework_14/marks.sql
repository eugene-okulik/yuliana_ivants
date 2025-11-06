SET @student_id = (SELECT id FROM students WHERE name = 'Yuliana' AND second_name = 'Ivantsova');

INSERT INTO marks (value, lesson_id, student_id)
SELECT '5', lessons.id, @student_id
FROM lessons
WHERE lessons.title = 'literature_begin';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '5', lessons.id, @student_id
FROM lessons
WHERE lessons.title = 'literature_profi';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '5', lessons.id, @student_id
FROM lessons
WHERE lessons.title = 'python and literature begin';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '5', lessons.id, @student_id
FROM lessons
WHERE lessons.title = 'python and literature profi';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '5', lessons.id, @student_id
FROM lessons
WHERE lessons.title = 'pythonx2 begin';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '5', lessons.id, @student_id
FROM lessons
WHERE lessons.title = 'pythonx2 profi';


SELECT *
FROM marks
ORDER BY id DESC
LIMIT 6;