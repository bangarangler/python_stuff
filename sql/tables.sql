-- CREATE TABLE dogs (
  -- name TEXT,
  -- breed TEXT,
  -- age INTEGER
-- )

-- INSERT INTO dogs (name, age, breed) VALUES("Champ", 4, "Husky")
-- INSERT INTO dogs (name, age, breed) VALUES("Rose", 11, "Chihuahua")
-- INSERT INTO dogs (name, age, breed) VALUES("Moose", 5, "Lab")
-- INSERT INTO dogs (name, age, breed) VALUES("Piggy", 9, "Corgi")
-- INSERT INTO dogs (name, age, breed) VALUES("Maggie", 4, "Terrier")
-- INSERT INTO dogs (name, age, breed) VALUES("River", 7, "Husky")
-- INSERT INTO dogs (name, age, breed) VALUES("Archer", 8, "Pitbul")
-- INSERT INTO dogs (name, age, breed) VALUES("Pam", 2, "Pug")

SELECT * FROM dogs;

SELECT name FROM dogs;

SELECT name, age FROM dogs;

SELECT * FROM dogs WHERE name IS "Piggy";

SELECT * FROM dogs WHERE breed IS "Husky";

SELECT name FROM dogs WHERE breed IS "Husky";

SELECT * FROM dogs WHERE breed IS NOT "Chihuahua" AND breed IS NOT "Pug";

SELECT * FROM dogs WHERE age > 8;

SELECT * FROM dogs WHERE name LIKE "%gg%";
