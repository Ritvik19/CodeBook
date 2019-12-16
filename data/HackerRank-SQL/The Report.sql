SELECT (CASE WHEN g.grade > 7 THEN s.name ELSE NULL END), g.grade, s.marks
FROM students s, grades g
WHERE s.marks BETWEEN g.min_mark AND g.max_mark
ORDER BY g.grade DESC, s.name, s.marks ASC;