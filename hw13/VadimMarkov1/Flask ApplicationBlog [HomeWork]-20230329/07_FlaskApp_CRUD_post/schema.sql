PRAGMA foreign_keys=on;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;


CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);


CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author TEXT NOT NULL,
    comment TEXT NOT NULL,
    posts_id INTEGER,
    FOREIGN KEY (posts_id)  REFERENCES posts (id) ON DELETE CASCADE
);

