CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name character varying(30) NOT NULL,
    second_name character varying(30) NOT NULL, 
    password TEXT NOT NULL,
    email TEXT,
    avatar_url Text,
    primary_cheerup_id INTEGER
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


INSERT INTO users(first_name, second_name, password, primary_cheerup_id) VALUES
    ('Ice', 'Cream', '*', 1);

INSERT INTO cheerups(user_id, cheerup, rating) VALUES (1, 'Sometimes the smallest step in the right direction ends up being the biggest step of your life. Tip toe if you must but take the step', 0);

INSERT INTO cheerups(user_id, cheerup, rating) VALUES (1, 'When everythin gfeels like an uphill struggle, just think of the view from the top', 0);

INSERT INTO cheerups(user_id, cheerup, rating) VALUES (1, 'Cheer up when the night comes, because morning always gives you another chance', 0);


-- https://www.quoteambition.com/cheer-up-quotes/

INSERT INTO avatar(user_id, url) VALUES (1, 'https://avatars.dicebear.com/api/male/john.svg?background=%230000ff');
