-- NOTE: altered script to insert valid email instead of
-- creating a new user field as it was already created
-- CREATE TABLE IF NOT EXISTS users (
    --  id int not null AUTO_INCREMENT,
    -- email varchar(255) not null,
    -- name varchar(255),
    -- valid_email boolean not null default 0,
    -- PRIMARY KEY (id)
-- );

-- insert new column instead
-- uncomment to run
-- ALTER TABLE users
-- ADD COLUMN valid_email BOOLEAN NOT NULL DEFAULT 0 AFTER name;

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);