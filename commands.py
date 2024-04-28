#!/usr/bin/env python3

import sqlite3
from api_call import insert_data_into_db
import click
import os
import threading
import itertools
import time
import sys

def spinner_animation(stop_event, message="Loading..."):
    """ Spinner function that runs until stop_event is set """
    for char in itertools.cycle('|/-\\'):
        if stop_event.is_set():
            # When stopping, overwrite the entire line with spaces and then return to the beginning
            sys.stdout.write('\r' + ' ' * (len(message) + 2) + '\r')
            sys.stdout.flush()
            break
        status = f"{message} {char}"
        sys.stdout.write(status)
        sys.stdout.flush()
        # Move back the cursor to the start of the line
        sys.stdout.write('\r')
        time.sleep(0.1)

def start_spinner():
    """ Start spinner animation in a separate thread """
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner_animation, args=(stop_event,))
    spinner_thread.start()
    return spinner_thread, stop_event

def stop_spinner(spinner_thread, stop_event):
    """ Stop the spinner animation """
    if spinner_thread:
        stop_event.set()
        spinner_thread.join()

@click.group()
def cli():
    """A CLI for searching Hacker News tables."""
    pass

DB_FILE = 'hacker_news.db'

def getdb(create=False):
    if os.path.exists(DB_FILE):
        if create:
            os.remove(DB_FILE)
    else:
        if not create:
            click.echo(click.style('No database found', fg='red'), err=True)
            sys.exit(1)
    con = sqlite3.connect(DB_FILE)
    con.execute('PRAGMA foreign_keys = ON')
    return con

@cli.command()
def refresh():
    """Refresh the database and get new data from hackerNews"""
    click.echo(click.style("\n╔═════════════════════════╗", fg='green', bold=True))
    click.echo(click.style("║ Starting refresh process║", fg='green', bold=True))
    click.echo(click.style("╚═════════════════════════╝\n", fg='green', bold=True))

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

    click.echo(click.style('\nDatabase created. Inserting data into tables...', fg='green'))
    print('+--------------+-----------------------------------+')
    print('|  table_name  |               total               |')
    print('+--------------+-----------------------------------+')
    spinner_thread, stop_event = start_spinner()
    insert_data_into_db()
    print('+--------------+-----------------------------------+')
    stop_spinner(spinner_thread, stop_event)
    click.echo(click.style("\n╔══════════════════════════════════╗", fg='green', bold=True))
    click.echo(click.style("║ Refresh complete. You're all set!║", fg='green', bold=True))
    click.echo(click.style("╚══════════════════════════════════╝\n", fg='green', bold=True))


def search_table(table_name, keywords):
    """Generic function to search a specified table with provided keywords."""
    conn = sqlite3.connect('hacker_news.db')
    cursor = conn.cursor()

    keyword_clauses = ' AND '.join([f"title LIKE ?" for _ in keywords])
    params = tuple(f'%{k}%' for k in keywords)

    if table_name == 'JobPostings':
        # Apply the keywords to both title and text
        keyword_clauses = f'({keyword_clauses}) AND ' + 'AND '.join([f"title LIKE ?" for _ in keywords])
        params *= 2  # Duplicate params for both title and text

    query = f"SELECT * FROM {table_name} WHERE {keyword_clauses}"
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    if results:
        for result in results:
            print('+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+')
            click.echo(click.style(str(result), fg='cyan') + "\n")
    else:
        click.echo(click.style("No results found.", fg='red'))

@cli.command()
@click.argument('keywords', nargs=-1, required=True)
def news(keywords):
    """Search by key in the NewsArticles table."""
    if keywords:
        key = [word + ' ' for word in keywords]
        search_table('NewsArticles', key)

@cli.command()
@click.argument('keywords', nargs=-1, required=True)
def shows(keywords):
    """Search by key in the Shows table."""
    if keywords:
        key = [word + ' ' for word in keywords]
        search_table('Shows', key)

@cli.command()
@click.argument('keywords', nargs=-1, required=True)
def jobs(keywords):
    """Search by key in the JobPostings table."""
    if keywords:
        key = [word + ' ' for word in keywords]
        search_table('JobPostings', key)

if __name__ == '__main__':
    cli()
