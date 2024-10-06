SELECT name --Which fields should be slected
FROM patrons; --Indicates table in which these fields are located

--You can then share this code with someone so they can query the same thing themselves

SELECT card_num, name --You can also select multiple fields from the table (can be in any order)
FROM patrons;

SELECT * --If you want to select all the fields you can use a * rather than writing them all out
FROM patrons;

SELECT name AS first_name, year_hired --Ailising / choosing name for column
FROM employees;

SELECT DISTINCT year_hired --In this case you would get a list with no duplicate values
FROM employees;

SELECT DISTINCT dept_id, year_hired --In this case with two distinct requests there would be no duplicates of a combination of them
FROM employees;

-- Views are similar to views in notion
CREATE VIEW employee_hire_years AS --Name of view
SELECT id, name, year_hired --What we want to select for the view
FROM employees; --The Table

SELECT id, name --Once a view is created, you can query it like a normal table
FROM employee_hire_years;