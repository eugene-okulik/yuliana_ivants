SET @student_id = (SELECT id FROM students WHERE name = 'Yuliana' AND second_name = 'Ivantsova');

SELECT *
FROM marks m 
WHERE m.student_id = @student_id

SELECT *
FROM books b 
WHERE b.taken_by_student_id = @student_id

SELECT s.name,
       s.second_name,
       g.title AS group_name,
       b.title       AS book_title,
       l.title       AS lesson_title,
       sub.title     AS subject_title,
       m.value       AS mark
FROM students s 
JOIN `groups` g on s.group_id = g.id
JOIN  books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = @student_id