import sqlite3
def create_tables():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                        id TEXT PRIMARY KEY,
                        make TEXT,
                        model TEXT,
                        year TEXT,
                        rent_per_day REAL,
                        available INTEGER
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        phone TEXT,
                        email TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        car_id TEXT,
                        customer_id TEXT,
                        days INTEGER,
                        total_rent REAL,
                        FOREIGN KEY(car_id) REFERENCES cars(id),
                        FOREIGN KEY(customer_id) REFERENCES customers(id)
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT,
                        role TEXT
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS employee(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      emp_name TEXT,
                      emp_salary REAL,
                      emp_Post TEXT,
                      emp_username TEXT,
                      emp_password TEXT
                      )''')
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('owner', 'owner123', 'owner')")
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('employee', 'emp123', 'employee')")
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES ('customer', 'cust123', 'customer')")

    conn.commit()
    conn.close()

def setup_database():
    create_tables()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    setup_database()
