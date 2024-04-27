import sqlite3
import click

DB_FILE = 'hacker_news.db'

def getdb(create=False):
    if os.path.exists(DB_FILE):
        if create:
            os.remove(DB_FILE)
    else:
        if not create:
            print('no database found')
            sys.exit(1)
    con = sqlite3.connect(DB_FILE)
    con.execute('PRAGMA foreign_keys = ON')
    return con

@click.command()
def create():
    with getdb(create=True) as con:
        con.execute(
'''CREATE TABLE NewsArticles (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT,
    author TEXT,
    points INTEGER,
    time INTEGER,
    comments_count INTEGER
)''')

        con.execute(
'''CREATE TABLE Shows (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT,
    author TEXT,
    points INTEGER,
    time INTEGER,
    comments_count INTEGER
)''')

        con.execute(
'''CREATE TABLE JobPostings (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT,
    author TEXT,
    time INTEGER,
    text TEXT
)''')

    print('database created')


# Establish a group for the commands
@click.group()
def cli():
    """A CLI for searching Hacker News tables."""
    pass

def search_table(table_name, keywords):
    """Generic function to search a specified table with provided keywords."""
    conn = sqlite3.connect('hacker_news_data.db')
    cursor = conn.cursor()

    keyword_clauses = ' AND '.join([f"title LIKE ?" for _ in keywords])
    params = tuple(f'%{k}%' for k in keywords)

    if table_name == 'JobPostings':
        # Apply the keywords to both title and text
        keyword_clauses = f'({keyword_clauses}) AND ' + 'AND '.join([f"text LIKE ?" for _ in keywords])
        params *= 2  # Duplicate params for both title and text

    query = f"SELECT * FROM {table_name} WHERE {keyword_clauses}"
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    if results:
        for result in results:
            print(result, "\n")
    else:
        print("No results found.")

@cli.command()
@click.argument('keywords', nargs=-1, required=True)
def news(keywords):
    """Search in the NewsArticles table."""
    if keywords:
        search_table('NewsArticles', keywords)

@cli.command()
@click.argument('keywords', nargs=-1, required=True)
def shows(keywords):
    """Search in the Shows table."""
    if keywords:
        search_table('Shows', keywords)

@cli.command()
@click.argument('keywords', nargs=-1, required=True)
def jobs(keywords):
    """Search in the JobPostings table."""
    if keywords:
        search_table('JobPostings', keywords)

if __name__ == '__main__':
    cli()

'''
import sqlite3
import click

@click.command()
@click.argument('table_name', type=click.Choice(['NewsArticles', 'Shows', 'JobPostings'], case_sensitive=False))
@click.argument('keyword')
def search_by_keyword(table_name, keyword):
    print(f"Filtering  {table_name} by {keyword}...\n")
    keyword = keyword + " "
    """Searches for the keyword in the specified table within the title or description fields."""
    # Connect to the SQLite database
    conn = sqlite3.connect('hacker_news_data.db')
    cursor = conn.cursor()

    # Prepare the SQL query based on the table
    if table_name in ['NewsArticles', 'Shows']:
        query = f"""
        SELECT * FROM {table_name}
        WHERE title LIKE ?
        """
        params = ('%' + keyword + '%',)
    elif table_name == 'JobPostings':
        query = f"""
        SELECT * FROM {table_name}
        WHERE title LIKE ? OR text LIKE ?
        """
        params = ('%' + keyword + '%', '%' + keyword + '%')

    # Use parameterized query to avoid SQL injection
    cursor.execute(query, params)

    # Fetch and return the results
    results = cursor.fetchall()
    conn.close()

    if results:
        for result in results:
            print(result)
    else:
        print("No results found.")

if __name__ == '__main__':
    search_by_keyword()


import sqlite3
import click

@click.command()
@click.option('--table_name', type=click.Choice(['NewsArticles', 'Shows', 'JobPostings'], case_sensitive=False), required=True, help='Specify the table to search within.')
@click.option('--keyword1', required=True, help='Required keyword to search for in title or text.')
@click.option('--keyword2', default=None, help='Optional second keyword to search for in title or text.')
@click.option('--keyword3', default=None, help='Optional third keyword to search for in title or text.')
def search_by_keyword(table_name, keyword1, keyword2, keyword3):
    print(f"Filtering {table_name} by {keyword1}, {keyword2}, {keyword3}...\n")

    # Connect to the SQLite database
    conn = sqlite3.connect('hacker_news_data.db')
    cursor = conn.cursor()

    # Prepare the SQL query based on the table
    keywords = [keyword1, keyword2, keyword3]
    keywords = [k for k in keywords if k]  # Remove None values
    keyword_clauses = ' AND '.join([f"title LIKE ?" for _ in keywords])
    params = tuple(f'%{k}%' for k in keywords)

    if table_name in ['NewsArticles', 'Shows']:
        query = f"SELECT * FROM {table_name} WHERE {keyword_clauses}"
    elif table_name == 'JobPostings':
        # Apply the keywords to both title and text
        keyword_clauses += ' OR ' + ' OR '.join([f"text LIKE ?" for _ in keywords])
        params *= 2  # Duplicate params as they apply to both title and text
        query = f"SELECT * FROM {table_name} WHERE {keyword_clauses}"

    # Use parameterized query to avoid SQL injection
    cursor.execute(query, params)

    # Fetch and return the results
    results = cursor.fetchall()
    conn.close()

    if results:
        for result in results:
            print(result)
    else:
        print("No results found.")

if __name__ == '__main__':
    search_by_keyword()
'''
