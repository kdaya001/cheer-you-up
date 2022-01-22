CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name CHARACTER VARYING(30) NOT NULL,
    second_name CHARACTER VARYING(30) NOT NULL, 
    password TEXT NOT NULL,
    email TEXT,
    avatar_url Text,
    score INTEGER
);

CREATE TABLE cheerups (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    cheerup CHARACTER VARYING(139) NOT NULL, 
    rating INTEGER,
    weather CHARACTER VARYING(3),
    public_visible BOOLEAN,
    voters text[],
    timestamp timestamp DEFAULT CURRENT_TIMESTAMP 
);

ALTER TABLE cheerups
ADD CONSTRAINT fk_user
FOREIGN KEY(user_id)
REFERENCES users(id);
