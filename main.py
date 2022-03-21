# [SQLPY-49] 4. Музыкальный сервис
# к лекции «Select-запросы, выборки из одной таблицы»

# import psycopg2
import sqlalchemy
import pandas as pd

from tables_tools import create_tables
from tables_tools import create_relations
from tables_tools import drop_tables
from tables_tools import fill_tables
from tables_tools import selects_tasks


def connect_to_db(login, password, db_name):
    if "" in (login.strip(), password, db_name.strip()):
        print('Недостаточно данных для работы с базой данных!')
        quit(1)
    db = f'postgresql+psycopg2://{login}:{password}@localhost:5432/{db_name}'
    engine = sqlalchemy.create_engine(db)
    return {'database': db, 'engine': engine}


def print_selects(print_list):
    for task in print_list:
        print()
        print(task['task_name'])
        print(pd.DataFrame(task['select']))


if __name__ == '__main__':
    connect_about = connect_to_db('py49', '123456', 'py49_db')
    db_scheme = 'sqlpy49_task3_1'
    connection = connect_about['engine'].connect()
    connection.execute(f"SET SCHEMA '{db_scheme}';")

    # Задание 1:
    # Заполнить базу данных

    drop_tables(connection)
    create_tables(connection)
    create_relations(connection)
    fill_tables(connection)

    # Задание 2:
    # Написать SELECT-запросы и вывести информацию

    select_list = selects_tasks(connection)
    print_selects(select_list)

    connection.close()
