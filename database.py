# functions for connecting to database, performing create, read, update, delete operations
# storing and retrieving user information and scores

import sqlite3
from sqlite3 import Error

db_name = 'ttt_players.sqlite'


def connect_to_database(path):  # get path, connect to / create db and return connection
    connection = None
    try:
        connection = sqlite3.connect(path)
        print(f'-Connection to {path} SQLite database successful.')
    except Error as e:
        print(f"-The error '{e}' occurred.")

    return connection


def execute_query(connection, query):  # db cursor commit
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f'-Query {query[:20]}... executed successfully.')
    except Error as e:
        print(f"-The error '{e}' occurred.")

    connection.close()
    print('-Connection closed.')

# def execute_fetch() - if will be more fetches


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    wins INTEGER
);
"""


def login_user(username, password):  # idk maybe more optimized to not open new connection on each Login click
    connection = connect_to_database(db_name)
    cursor = connection.cursor()
    query = f"SELECT username, password FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchone()

    if result is not None:
        print('-User exists', result)
        if result[1] == password:
            login_status = 'Ok'
        else:
            print('-Wrong password')
            login_status = 'Wrong password'
    else:
        print('-User does not exist')
        login_status = 'User does not exist'

    connection.close()
    print('-Connection closed.')

    return login_status


# ADD USER record to db
# TODO fix connection, if can do with different execute (query + user/pass)
def register_user(username, password):
    connection = connect_to_database(db_name)
    query = """
    INSERT INTO
        users (username, password, wins)
    VALUES
        (?, ?, 0)
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (username, password))
        connection.commit()
        print(f'-Username {username} registered successfully.')
    except Error as e:
        print(f"-The error '{e}' occurred.")

    connection.close()
    print('-Connection closed.')

