INSERT INTO subjects (title)
VALUES ('literature'),
       ('python and literature'),
       ('pythonx2')
       
SELECT *
FROM subjects s 
ORDER BY id DESC
LIMIT 3;