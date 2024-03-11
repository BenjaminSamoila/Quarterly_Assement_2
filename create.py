import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create tables for each category
cursor.execute('''CREATE TABLE IF NOT EXISTS GeneralGeography
              (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS GeneralHistory
              (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Accounting
              (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Math
              (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Programming
              (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')

# Add data to each table
questions = [
    ('GeneralGeography', 'What is the capital of France?', 'Paris'),
    ('GeneralGeography', 'What is the largest continent?', 'Asia'),
    ('GeneralGeography', 'What is the longest river in the world?', 'Nile'),
    ('GeneralGeography', 'What is the largest desert in the world?', 'Sahara'),
    ('GeneralGeography', 'What is the highest mountain in the world?', 'Mount Everest'),
    ('GeneralGeography', 'Which country is known as the Land of the Rising Sun?', 'Japan'),
    ('GeneralGeography', 'What is the smallest country in the world?', 'Vatican City'),
    ('GeneralGeography', 'Which river runs through Baghdad?', 'Tigris'),
    ('GeneralGeography', 'What is the world\'s largest ocean?', 'Pacific'),
    ('GeneralGeography', 'Which country has the longest coastline in the world?', 'Canada'),
    ('GeneralHistory', 'In which year did World War II end?', '1945'),
    ('GeneralHistory', 'Who was the first President of the United States?', 'George Washington'),
    ('GeneralHistory', 'Which ancient civilization built the pyramids?', 'Egyptians'),
    ('GeneralHistory', 'Who was the first female Prime Minister of the United Kingdom?', 'Margaret Thatcher'),
    ('GeneralHistory', 'Which year was the Magna Carta signed?', '1215'),
    ('GeneralHistory', 'Who was the first man to step on the moon?', 'Neil Armstrong'),
    ('GeneralHistory', 'Who painted the Mona Lisa?', 'Leonardo da Vinci'),
    ('GeneralHistory', 'Who was the last tsar of Russia?', 'Nicholas II'),
    ('GeneralHistory', 'Who wrote the Communist Manifesto?', 'Karl Marx'),
    ('Accounting', 'What is the formula for calculating net income?', 'Revenue - Expenses'),
    ('Accounting', 'What is the principle of double-entry bookkeeping?', 'Every financial transaction has equal and opposite effects in at least two different accounts.'),
    ('Accounting', 'What is the formula for calculating return on investment (ROI)?', '(Net Profit / Cost of Investment) x 100'),
    ('Accounting', 'What is the abbreviation for the accounting equation?', 'A = L + E (Assets = Liabilities + Equity)'),
    ('Accounting', 'What is the purpose of an income statement?', 'To show the profitability of a company over a specific period of time.'),
    ('Accounting', 'What is the purpose of a balance sheet?', 'To show the financial position of a company at a specific point in time.'),
    ('Accounting', 'What is the purpose of a cash flow statement?', 'To show the inflows and outflows of cash and cash equivalents in a company.'),
    ('Accounting', 'What is the formula for calculating gross profit?', 'Revenue - Cost of Goods Sold'),
    ('Accounting', 'What is the difference between financial accounting and managerial accounting?', 'Financial accounting is focused on external reporting to investors, creditors, and regulators, while managerial accounting is focused on providing information to internal users for decision-making.'),
    ('Accounting', 'What is the purpose of the Sarbanes-Oxley Act?', 'To improve corporate governance and prevent accounting scandals.'),
    ('Math', 'What is the value of pi (π) to two decimal places?', '3.14'),
    ('Math', 'What is the square root of 64?', '8'),
    ('Math', 'What is the value of 5 factorial (5!)?', '120'),
    ('Math', 'What is the Pythagorean theorem?', 'In a right-angled triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides.'),
    ('Math', 'What is the formula for the area of a circle?', 'πr^2'),
    ('Math', 'What is the formula for the volume of a sphere?', '(4/3)πr^3'),
    ('Math', 'What is the formula for calculating the slope of a line?', '(y2 - y1) / (x2 - x1)'),
    ('Math', 'What is the difference between permutation and combination?', 'Permutation considers the arrangement of objects, while combination considers the selection of objects without regard to the order.'),
    ('Math', 'What is the Fibonacci sequence?', 'A series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1.'),
    ('Math', 'What is Euler\'s number (e)?', 'Approximately 2.71828'),
    ('Programming', 'What does HTML stand for?', 'HyperText Markup Language'),
    ('Programming', 'What is the output of 2 + 3 * 4?', '14'),
    ('Programming', 'What is the purpose of a variable in programming?', 'To store and manipulate data.'),
    ('Programming', 'What is a conditional statement in programming?', 'A statement that performs different actions depending on whether a condition is true or false.'),
    ('Programming', 'What is a loop in programming?', 'A control structure that repeats a block of code until a specified condition is met.'),
    ('Programming', 'What is the difference between a function and a method in programming?', 'A function is a piece of code that is called by name and can be passed arguments and return data, while a method is a function associated with an object.'),
    ('Programming', 'What is the purpose of the "if" statement in programming?', 'To execute a block of code only if a specified condition is true.'),
    ('Programming', 'What is the purpose of the "for" loop in programming?', 'To iterate over a sequence (e.g., a list, tuple, or string) a specified number of times.'),
    ('Programming', 'What is the purpose of the "while" loop in programming?', 'To repeatedly execute a block of code as long as a specified condition is true.'),
    ('Programming', 'What is the difference between "==" and "=" in programming?', '"==" is a comparison operator used to compare two values for equality, while "=" is an assignment operator used to assign a value to a variable.')
]

for question in questions:
    cursor.execute(f"INSERT INTO {question[0]} (question, answer) VALUES (?, ?)", (question[1], question[2]))

conn.commit()
conn.close()