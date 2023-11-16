import csv
from classes.Database import Database

def export_to_csv(table_name):
        table_data = Database.get_table_data(table_name)
        # write the actual element's colums and rows to the CSV
        try:
            with open(f"{table_name}.csv" , mode = "w", newline = "\n", encoding = "utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(table_data["columns"])
                writer.writerows(table_data["rows"])
        except Exception as error:
            print(f"Error: {error}")
