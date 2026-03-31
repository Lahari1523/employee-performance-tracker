import sqlite3

def add_employee(name, department, month, score):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, department, month, performance_score) VALUES (?, ?, ?, ?)',
                   (name, department, month, score))
    conn.commit()
    conn.close()
    print(f"Added {name}'s record successfully.")

def view_all():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    conn.close()
    return rows

def top_performers():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, MAX(performance_score) FROM employees GROUP BY department')
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    add_employee("Alice", "Engineering", "March", 90)
    add_employee("Bob", "Marketing", "March", 85)

    print("All Employees:")
    for r in view_all():
        print(r)

    print("\nTop Performers by Department:")
    for r in top_performers():
        print(r)
