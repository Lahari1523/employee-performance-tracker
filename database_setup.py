import sqlite3

conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    month TEXT,
    performance_score INTEGER
)
''')

conn.commit()
conn.close()
print("Database and table created successfully.")
