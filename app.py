import sqlite3

def display_feedback(is_correct):
    if is_correct:
        print("\033[92mCorrect!\033[0m\n")
    else:
        print("\033[91mWrong! Try again.\033[0m\n")

def play_quiz(category):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT question, answer FROM {category};")
    questions = cursor.fetchall()

    for question, answer in questions:
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.lower() == answer.lower():
            display_feedback(True)
        else:
            display_feedback(False)

    conn.close()

def main():
    print("Categories:")
    print("1. General Geography")
    print("2. General History")
    print("3. Accounting")
    print("4. Math")
    print("5. Programming")

    category_map = {
        '1': 'GeneralGeography',
        '2': 'GeneralHistory',
        '3': 'Accounting',
        '4': 'Math',
        '5': 'Programming'
    }

    while True:
        choice = input("Select a category (1-5): ")
        if choice in category_map:
            category = category_map[choice]
            play_quiz(category)
            break
        else:
            print("Invalid choice. Please select a valid category.")

if __name__ == "__main__":
    main()