SELECT h.hacker_id, name, SUM(score) AS total_score
FROM
    hackers AS h INNER JOIN
    (SELECT hacker_id, MAX(score) AS score
    FROM submissions
    GROUP BY challenge_id, hacker_id) max_score
    ON h.hacker_id=max_score.hacker_id
GROUP BY h.hacker_id, name
HAVING total_score > 0
ORDER BY total_score DESC, h.hacker_id;