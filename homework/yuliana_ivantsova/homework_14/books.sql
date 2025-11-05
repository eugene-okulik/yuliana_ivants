SET @student_id = (SELECT id FROM students WHERE name = 'Yuliana' AND second_name = 'Ivantsova');

INSERT INTO books (title, taken_by_student_id)
VALUES 
  ('Капля духов в открытую рану', @student_id),
  ('Ученик убийцы', @student_id),
  ('И жили они долго и счастливо', @student_id),
  ('Подросток', @student_id);

SELECT  * 
FROM books b 
WHERE b.taken_by_student_id = @student_id;
