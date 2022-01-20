INSERT INTO users (first_name, last_name, email) VALUES('Stephen', 'C', 'test@email.com');
INSERT INTO users (first_name, last_name, email) VALUES('Dojo', 'Ninja', 'ninja@coding.dojo');
INSERT INTO users (first_name, last_name, email) VALUES('John', 'Doe', 'johnd@gmail.com');

SELECT * FROM users;

SELECT * FROM users WHERE email='test@email.com';

SELECT * FROM users WHERE id=3;

DELETE FROM users WHERE id=2;

SELECT * FROM users ORDER BY first_name;
SELECT * FROM users ORDER BY first_name DESC;