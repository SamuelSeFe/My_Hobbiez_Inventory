DROP TABLE IF EXISTS hobbies;
DROP TABLE IF EXISTS locations;

CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  distance_to_location INT,
  reminder TEXT
);

CREATE TABLE hobbies (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  activity_area VARCHAR(255),
  duration INT,
  cost FLOAT,
  energy_expenditure INT,
  completed BOOLEAN,
  location_id INT NOT NULL REFERENCES location(id) ON DELETE CASCADE,
  reminder TEXT
);

