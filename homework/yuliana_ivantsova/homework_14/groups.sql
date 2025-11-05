INSERT INTO `groups` (title, start_date, end_date)
SELECT 'AQA and literature', '01.01.2026', '01.05.2027'
WHERE NOT EXISTS(
SELECT *
FROM `groups` 
WHERE title = 'AQA and literature' AND end_date = '01.05.2027'
)


SELECT *
FROM `groups` g
WHERE title = 'AQA and literature' AND end_date = '01.05.2027'