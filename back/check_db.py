import json
import psycopg2
from psycopg2 import Error
from password import DB_CONNECT_LOCAL

try:
    connection = psycopg2.connect(
        user=DB_CONNECT_LOCAL.get("user"),
        password=DB_CONNECT_LOCAL.get("password"),
        host=DB_CONNECT_LOCAL.get("host"),
        port=DB_CONNECT_LOCAL.get("port"),
        database=DB_CONNECT_LOCAL.get("database")
    )
    cursor = connection.cursor()
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")
    cursor.execute("SELECT * FROM plans")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
