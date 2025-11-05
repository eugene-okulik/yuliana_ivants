INSERT INTO lessons (title, subject_id)
VALUES ('literature_begin', 12797),
       ('literature_profi', 12797),
       ('python and literature begin', 12796),
       ('python and literature profi', 12796),
       ('pythonx2 begin', 12795),
       ('pythonx2 profi', 12795)
       
       
 SELECT *
FROM lessons
ORDER BY id DESC
LIMIT 6;