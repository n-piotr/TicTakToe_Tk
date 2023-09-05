from database import db_name, connect_to_database, execute_query, create_users_table
from ui import draw_interface
from game import start_game


def main():
    connection = connect_to_database(db_name)
    execute_query(connection, create_users_table)  # create table if not exists

    draw_interface()

    start_game()


if __name__ == '__main__':
    main()
