#!/usr/bin/env python3

# env looks for excecutable of the name I type after just in case its installed
# in different places

# Social Network (tables and their connections are in a drawing)
import click
import sqlite3
# To work with timestamps.
from datetime import datetime
import os
import sys

if not os.path.exists:
    print("Database not found")
    sys.exit(1)

# Connect to the SQLite database
conn = sqlite3.connect('network.db')
cursor = conn.cursor()

@click.group()
def cli():
    pass

# Email is REQUIRED
@click.command()
@click.argument('email')
@click.option('--phone_number', default=None, help='Your phone number')
@click.option('--birthday', default=None, help='Your birthday')
# TODO Do i need the default to None still?
# TODO How do I restrict creatind a user with an existing email?
def createUser(email, phone_number=None, birthday=None):
    print('creating user with email address', email)
    # Add a new user to the USERS table
    cursor.execute("INSERT INTO USERS (email, phone_number, birthday) VALUES (?, ?, ?)",
                   (email, phone_number, birthday))
    conn.commit()
    # Since we inserted before we want to assign the id that was generated to
    # the user_id, that is why we use .lastrowid
    user_id = cursor.lastrowid
    print(f'user inserted with id = {user_id}, email = {email}, phone number = {phone_number}, and birthday = {birthday}')

    return user_id

# User created and username are REQUIRED
@click.command()
@click.argument('email')
@click.argument('username')
# TODO Privacy doens't work idk how to implement it
@click.option('--privacy', default=None, help='Privacy settings')
# TODO Do i need the default to None still?
def createAccount(email, username, privacy=None):
    print('creating account with username', username, 'for email', email)
    # Add a new account to the ACCOUNTS table
    cursor.execute("""INSERT INTO ACCOUNTS (user_id, username, privacy_settings)
                   VALUES ((SELECT user_id FROM USERS WHERE email = ?), ?, ?)""",
                   (email, username, privacy))
    conn.commit()
    account_id = cursor.lastrowid
    print(f'account inserted with id = {account_id}, for email = {email} with username = {username}. \nPrivacy settings are set to = {privacy}')

    return account_id

@click.command()
@click.argument('follower_username')
@click.argument('followee_username')
# Followee -> account_id that is followed Follower -> account_id that followed 
def follow(follower_username, followee_username):
    # Add a new follow relationship to the FOLLOWERS table
    cursor.execute("""INSERT INTO FOLLOWERS (follower_account_id,
                   followee_account_id) VALUES ((SELECT account_id FROM
                   ACCOUNTS WHERE username = ?),(SELECT account_id FROM ACCOUNTS
                   WHERE username = ?))""",
                   (follower_username, followee_username))
    print(f'{follower_username} now follows: {followee_username}')
    conn.commit()

@click.command()
@click.argument('account_username')
@click.argument('post_text')
# Posts are ONLY text and ir REQUIRES the account related to and the post itself
def post(account_username, post_text):
    # Add a new post to the POSTS table
    cursor.execute("""INSERT INTO POSTS (account_id, post_text) VALUES ((SELECT
                   account_id FROM ACCOUNTS WHERE username = ?), ?)""",
                   (account_username, post_text))
    conn.commit()
    print(f'{account_username} posted: {post_text}')

@click.command()
@click.argument('liker_username')
@click.argument('post_username')
@click.argument('post_id', type=int)
def like(liker_username, post_username, post_id):
    # Add a new like to the LIKES table
    cursor.execute("""INSERT INTO LIKES (post_id, account_id)
                   VALUES (?, (SELECT account_id FROM ACCOUNTS WHERE username = ?))""",
                   (post_id, liker_username))
    conn.commit()
    print(f'{liker_username} liked {post_username} post')

@click.command()
@click.argument('commenter_username')
@click.argument('post_username')
@click.argument('post_id', type=int)
@click.argument('comment_text')
def comment(commenter_username, post_username, post_id, comment_text):
    # Add a new comment to the COMMENTS table
    cursor.execute("""INSERT INTO COMMENTS (post_id, account_id, comment_text)
                   VALUES (?, (SELECT account_id FROM ACCOUNTS WHERE username = ?), ?)""",
                   (post_id, commenter_username, comment_text))
    conn.commit()
    print(f'You commented: {comment_text} to {post_username}')

@click.command()
@click.argument('account_username')
def displayFeed(account_username):
    # Display the most recent posts of accounts the user follows
    rows = cursor.execute("""
        SELECT * FROM ACCOUNTS me
        JOIN FOLLOWERS ON me.account_id = follower_account_id
        JOIN POSTS ON followee_account_id = posts.account_id
        JOIN ACCOUNTS them ON followee_account_id = them.account_id
        WHERE  me.username = ?
        ORDER BY them.timestamp DESC
        LIMIT 10;
        """, (account_username,))

    rows = cursor.fetchall()

    # 8, 10, 13
    for row in rows:
        # Assuming the columns are in the following order: username, timestamp, post_text
        post_id = row[8]  
        post_text = row[10] 
        username = row[13]  
        print(f'People you follow: {username}, Post id: {post_id}, Post text: {post_text}')

'''
def suggestAccounts(account_id):
    # Suggestions based on common followers and common accounts followed
    cursor.execute("""
        SELECT DISTINCT A.account_id, A.username
        FROM FOLLOWERS F1
        JOIN FOLLOWERS F2 ON F1.follower_account_id = F2.follower_account_id
        JOIN ACCOUNTS A ON (
            (F2.followee_account_id = A.account_id AND F1.followee_account_id = ?)
            OR
            (F2.follower_account_id = A.account_id AND F1.follower_account_id = ?)
        )
        WHERE A.account_id NOT IN (SELECT followee_account_id FROM FOLLOWERS WHERE follower_account_id = ?)
        AND F2.follower_account_id != ?
        LIMIT 5
    """, (account_id, account_id, account_id, account_id))

    suggestions = cursor.fetchall()

    return suggestions
'''

cli.add_command(createUser)
cli.add_command(createAccount)
cli.add_command(follow)
cli.add_command(post)
cli.add_command(like)
cli.add_command(comment)
cli.add_command(displayFeed)
# cli.add_command(suggestAccounts)

cli()
