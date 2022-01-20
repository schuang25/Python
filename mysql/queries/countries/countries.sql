-- Query 1
SELECT name, language, percentage FROM countries 
JOIN languages ON countries.id = languages.country_id
WHERE language = 'Slovene'
ORDER BY percentage DESC;

-- Query 2 
-- 7 "countries" do not have any cities, so a left join would return 239 rows instead of the expected 232.
SELECT countries.name, COUNT(cities.id) as cities FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.id) DESC;

-- Query 3
SELECT cities.name, cities.population, cities.country_id FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.population > 500000 AND countries.name = 'Mexico'
ORDER BY cities.population DESC;

-- Query 4
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages on countries.id = languages.country_id
WHERE languages.percentage > 89.0
ORDER BY languages.percentage DESC;

-- Query 5
SELECT name, surface_area, population FROM countries
WHERE surface_area < 501.0 AND population > 100000;

-- Query 6
SELECT name, government_form, capital, life_expectancy FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75.0;

-- Query 7
SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.district = 'Buenos Aires' AND cities.population > 500000
ORDER BY cities.population DESC;

-- Query 8
SELECT region, COUNT(region) AS countries FROM countries
GROUP BY region
ORDER BY COUNT(region) DESC;