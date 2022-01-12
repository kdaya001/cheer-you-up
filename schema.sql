CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name character varying(30) NOT NULL,
    second_name character varying(30) NOT NULL, 
    password TEXT NOT NULL,
    primary_cheerup_id INTEGER
);

CREATE TABLE cheerups (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    cheerup TEXT, 
    rating INTEGER
);

CREATE TABLE avatar (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    url TEXT
);

ALTER TABLE cheerups
ADD CONSTRAINT fk_user
FOREIGN KEY(user_id)
REFERENCES users(id);

ALTER TABLE avatar
ADD CONSTRAINT fk_user
FOREIGN KEY(user_id)
REFERENCES users(id);


INSERT INTO users(first_name, second_name, password, primary_cheerup_id) VALUES
    ('Ice', 'Cream', '*', 1);

INSERT INTO cheerups(user_id, cheerup, rating) VALUES (1, 'hello world', 3);

INSERT INTO avatar(user_id, url) VALUES (1, 'https://avatars.dicebear.com/api/male/john.svg?background=%230000ff');
