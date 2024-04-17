-- If questions refer the drawing

-- USERS table
CREATE TABLE USERS (
    user_id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    phone_number TEXT,
    birthday DATE,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX users_email
ON USERS (email);

-- ACCOUNTS table
CREATE TABLE ACCOUNTS (
    account_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    --DEL. CASCADE takes care of deleting related things
    user_id INTEGER REFERENCES USERS(user_id) ON DELETE CASCADE,
    privacy_settings TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX account_username
ON ACCOUNTS (username);

-- FOLLOWERS table
CREATE TABLE FOLLOWERS (
    follower_account_id INTEGER REFERENCES ACCOUNTS(account_id) ON DELETE CASCADE,
    followee_account_id INTEGER REFERENCES ACCOUNTS(account_id) ON DELETE CASCADE,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (follower_account_id, followee_account_id)
);

-- POSTS table
CREATE TABLE POSTS (
    post_id INTEGER PRIMARY KEY,
    account_id INTEGER REFERENCES ACCOUNTS(account_id) ON DELETE CASCADE,
    post_text TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- LIKE table (additional)
CREATE TABLE LIKES (
    post_id INTEGER REFERENCES POSTS(post_id) ON DELETE CASCADE,
    account_id INTEGER REFERENCES ACCOUNTS(account_id) ON DELETE CASCADE,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (post_id, account_id)
);

-- COMMENTS table (additional)
CREATE TABLE COMMENTS (
    comment_id INTEGER PRIMARY KEY,
    post_id INTEGER REFERENCES POSTS(post_id) ON DELETE CASCADE,
    account_id INTEGER REFERENCES ACCOUNTS(account_id) ON DELETE CASCADE,
    comment_text TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

