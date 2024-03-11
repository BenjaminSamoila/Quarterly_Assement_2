import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
table_names = [table[0] for table in tables]

# Get all data from each table
for table_name in table_names:
    cursor.execute(f"SELECT * FROM {table_name};")
    data = cursor.fetchall()
    print(f"Table: {table_name}")
    for row in data:
        print(row)

conn.close()
