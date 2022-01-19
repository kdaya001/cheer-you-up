CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name character varying(30) NOT NULL,
    second_name character varying(30) NOT NULL, 
    password TEXT NOT NULL,
    email TEXT,
    avatar_url Text,
    score = INTEGER
);

CREATE TABLE cheerups (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    cheerup character varying(139) NOT NULL, 
    rating INTEGER
    weather character varying(3)
);

ALTER TABLE cheerups
ADD CONSTRAINT fk_user
FOREIGN KEY(user_id)
REFERENCES users(id);

ALTER TABLE cheerups 
ADD COLUMN timestamp timestamp default current_timestamp;