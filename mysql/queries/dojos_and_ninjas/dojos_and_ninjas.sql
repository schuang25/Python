INSERT INTO dojos (name) VALUES ('SF Bay Area');
INSERT INTO dojos (name) VALUES ('Chicago');
INSERT INTO dojos (name) VALUES ('Online');

-- bypass safe updates but also turn it back on to stay safe
SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;
SET SQL_SAFE_UPDATES = 1;

-- add id otherwise AI assigns to 4, 5, 6
INSERT INTO dojos (name, id) VALUES ('Seattle', 1);
INSERT INTO dojos (name, id) VALUES ('SF Bay Area', 2);
INSERT INTO dojos (name, id) VALUES ('Online', 3);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES('Ninja', 'One', 23, 1);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES('Ninja', 'Two', 25, 1);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES('Ninja', 'Three', 21, 1);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES('Ninja', 'Four', 24, 2);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES('Ninja', 'Five', 22, 2);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES('Ninja', 'Six', 26, 2);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES('Ninja', 'Seven', 28, 3);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES('Ninja', 'Eight', 29, 3);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES('Ninja', 'Nine', 27, 3);

SELECT * FROM ninjas WHERE dojo_id=1;

SELECT * FROM ninjas WHERE dojo_id=3;

SELECT * FROM dojos WHERE id=(SELECT dojo_id FROM ninjas ORDER BY ninjas.id DESC LIMIT 1);