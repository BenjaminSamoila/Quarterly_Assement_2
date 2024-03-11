import sqlite3

# Connect to the database file
conn = sqlite3.connect('FridayProj5.db')
cursor = conn.cursor()

# Get the name of the table in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_name = cursor.fetchone()[0]

# Retrieve questions and answers from the database table
cursor.execute(f"SELECT question, answer FROM {table_name};")
questions = cursor.fetchall()

# Iterate over the retrieved questions and answers
for question, answer in questions:
    print(question)
    user_answer = input("Your answer: ")
    
    if user_answer.lower() == answer.lower():
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {answer}\n")

# Close the database connection
conn.close()