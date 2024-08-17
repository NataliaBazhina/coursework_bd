import psycopg2
from config import config


def setup_connection():
    """Устанавливает соединение с базой данных PostgreSQL"""
    params = config()
    try:
        with psycopg2.connect(**params) as conn:
            conn.autocommit = True
            return conn
    except psycopg2.Error as e:
        print(f"PostgreSQL error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_database(database_name: str, conn: psycopg2.extensions.connection):
    """Создает базу данных"""
    with conn.cursor() as cur:
        cur.execute(f'CREATE DATABASE {database_name}'
                    )


def create_tables(database_name: str, conn: psycopg2.extensions.connection):
    """Создает таблицы"""
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


def inspect_salary_from(vacancy: dict):
    """обрабатывает заработную плату"""
    if vacancy["salary"] is None:
        return 0
    if isinstance(vacancy["salary"], int):
        return vacancy["salary"]
    if isinstance(vacancy["salary"], str):
        if vacancy["salary"].lower() in ['зарплата не указана', 'не указана']:
            return 0

        cleaned_salary = vacancy["salary"].replace(' ', '').replace('руб.', '').replace('руб', '')
        try:
            return int(cleaned_salary)
        except ValueError:
            return 0
    if isinstance(vacancy["salary"], dict):
        salary_from = vacancy["salary"].get('from')
        salary_to = vacancy["salary"].get('to')
        if salary_from and salary_to:
            return (salary_from + salary_to) // 2
        return salary_from if salary_from else salary_to if salary_to else 0
    return 0

# Example usage:
# conn = psycopg2.connect("your_connection_string")
# create_tables("my_new_database", conn)
# conn.close()
#
# conn = setup_connection()
# create_database("employers", conn)


# create_tables('vacancies', conn)
