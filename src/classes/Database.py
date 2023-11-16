import mysql.connector
from config import db_config

class Database:
    @staticmethod
    def get_table_list():
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            cursor.execute("SHOW TABLES")
            return [table[0] for table in cursor.fetchall()]
        except mysql.connector.Error as error:
            print(f"Error: {error}")
        finally:
            if connection and connection.is_connected():
                if cursor:
                    cursor.close()
                connection.close()

    @staticmethod
    def get_table_data(table_name):
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # get all data from the table
            cursor.execute(f"SELECT * FROM {table_name};")
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            return {"columns": columns, "rows": rows}
        except mysql.connector.Error as error:
            print(f"Error: {error}")
        finally:
            if connection and connection.is_connected():
                if cursor:
                    cursor.close()
                connection.close()