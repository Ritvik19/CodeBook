SELECT a.id, b.age, a.coins_needed, a.power
FROM Wands a INNER JOIN Wands_Property b ON a.code=b.code
WHERE b.is_evil!=1 AND a.coins_needed=(SELECT min(Wands.coins_needed)
    FROM Wands INNER JOIN Wands_Property ON Wands.code=Wands_Property.code
    WHERE Wands_Property.age=b.age AND Wands.power=a.power)
ORDER BY a.power DESC,b.age DESC;