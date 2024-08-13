import psycopg2
from config import config


def setup_connection():
    params = config()
    try:
        with psycopg2.connect(**params) as conn:
            conn.autocommit = True
            return conn
    except psycopg2.Error as e:
        print(f"PostgreSQL error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def create_database(database_name: str, conn:psycopg2.extensions.connection):
    with conn.cursor() as cur:
        cur.execute(f'CREATE DATABASE {database_name}'
        )


def create_tables(database_name: str, conn: psycopg2.extensions.connection):
    try:
        conn.autocommit = True
        with conn.cursor() as cur:
            with open('migrations.sql', 'r') as f:
                sql_commands = f.read()
            sql_commands_list = sql_commands.split(';')
            for command in sql_commands_list:
                command = command.strip()
                if command:
                    cur.execute(command)
            print(f"Таблицы успешно созданы в базе данных '{database_name}'.")
    except psycopg2.Error as e:
        print(f"Ошибка при создании таблиц: {e}")
    finally:
        conn.autocommit = False


# Example usage:
# conn = psycopg2.connect("your_connection_string")
# create_tables("my_new_database", conn)
# conn.close()
#
# conn = setup_connection()
# create_database("employers", conn)


# create_tables('vacancies', conn)

