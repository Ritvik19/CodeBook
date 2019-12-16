SELECT co.continent, FLOOR(AVG(c.population))
FROM city c, COUNTRY co
WHERE c.countrycode = co.code
GROUP BY co.continent;