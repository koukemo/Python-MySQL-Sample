CREATE TABLE IF NOT EXISTS users
(
    id serial,
    name varchar(50) NOT NULL,
    email varchar(256) NOT NULL,
    PRIMARY KEY (id)
);