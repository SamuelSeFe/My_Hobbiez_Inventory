DROP TABLE IF EXISTS hobbies;
DROP TABLE IF EXISTS locations;

CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  distance_to_location INT
);

CREATE TABLE hobbies (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  time_taken INT,
  cost_of_hobby FLOAT,
  energy_expenditure INT,
  completed BOOLEAN,
  location_id INT NOT NULL REFERENCES location(id) ON DELETE CASCADE,
  reminder TEXT
);

