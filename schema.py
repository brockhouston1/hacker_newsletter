
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('hacker_news_data.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE NewsArticles (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT,
    author TEXT,
    points INTEGER,
    time INTEGER,
    comments_count INTEGER
)
''')

cursor.execute('''
CREATE TABLE Shows (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT,
    author TEXT,
    points INTEGER,
    time INTEGER,
    comments_count INTEGER
)
''')

cursor.execute('''
CREATE TABLE JobPostings (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT,
    author TEXT,
    time INTEGER,
    text TEXT
)
''')

cursor.execute('''
CREATE TABLE MyList (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT,
    author TEXT,
    points INTEGER,
    time INTEGER,
    comments TEXT,
    text TEXT
)
''')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
