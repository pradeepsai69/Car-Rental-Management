import sqlite3
from db_setup import setup_database

class CarRentalSystem:
    def __init__(self):
        self.conn = sqlite3.connect('car_rental.db')
        self.cursor = self.conn.cursor()

    def login(self, role):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=? AND role=?", (username, password, role))
        user = self.cursor.fetchone()
        if user:
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid credentials.")
            return False

# Owner Interface
    def addadmin(self):
        admin={
            'username':input("Enter Username for admin: "),
            'password':input("Assign password for admin: "),
            'role':"owner"
        }
        self.cursor.execute("INSERT INTO users VALUES(?,?,?)",(admin['username'],admin['password'],admin['role']))
        self.conn.commit()
        print("Admin added succesfully")
    def add_car(self):
        
        car = {
            'id': input("Enter car ID: "),
            'make': input("Enter car make: "),
            'model': input("Enter car model: "),
            'year': input("Enter car year: "),
            'rent_per_day': float(input("Enter rent per day: ")),
            'available': 1
        }
        self.cursor.execute("INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?)",
                            (car['id'], car['make'], car['model'], car['year'], car['rent_per_day'], car['available']))
        self.conn.commit()
        print("Car added successfully.")
    def delemployee(self):
        eid=input("Enter emp Id You Need to delete: ")
        sql_update="""DELETE from emplyoee where id=?"""
        self.cursor.execute(sql_update,(eid,))
        self.conn.commit()
        print("Record Deleted Successfully")
        
    def deletecar(self):
        cid=input("Enter car Id You Need to delete: ")
        sql_update="""DELETE from cars where id=?"""
        self.cursor.execute(sql_update,(cid,))
        self.conn.commit()
        print("Record Deleted Successfully")
    def deleteemployee(self):
        eid=input("Enter Employee Id You Need to delete: ")
        sql_update="""DELETE from employee where id=?"""
        self.cursor.execute(sql_update,(eid,))
        self.conn.commit()
        print("Record Deleted Successfully")
    def view_cars(self):
        self.cursor.execute("SELECT * FROM cars")
        cars = self.cursor.fetchall()
        print("\nCar Inventory:")
        for car in cars:
            print(car)

    def view_employees(self):
        self.cursor.execute("SELECT * FROM users WHERE role='employee'")
        employees = self.cursor.fetchall()
        print("\nEmployee List:")
        for employee in employees:
            print(employee)

    def add_employee(self):
        employee = {
            'emp_name':input("Enter employee name: "),
            'emp_id':input("Assign Employee Id: "),
            'emp_salary':float(input("Enter employee salary")),
            'emp_post':input("Assign post to the employee"),
            'username': input("Enter employee username: "),
            'password': input("Enter employee password: "),
            'role':"employee"
        }
        self.cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (employee['id'], employee['emp_name'], employee['emp_salary'],employee['emp_post'],employee['username'],employee['password']))
        self.cursor.execute("INSERT INTO users VALUES(?,?,?)",(employee['username'],employee['password'],employee['role']))
        self.conn.commit()
        print("Employee added successfully.")

    def view_customers(self):
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()
        print("\nCustomer List:")
        for customer in customers:
            print(customer)
# Employee Interface
    def register_customer(self):
        customer = {
            'id': input("Enter customer ID: "),
            'name': input("Enter customer name: "),
            'phone': input("Enter customer phone: "),
            'email': input("Enter customer email: "),
            'username':input("Enter Customer Username: "),
            'Password':input("Create a Password: ")
        }
        self.cursor.execute("INSERT OR IGNORE INTO users(username, password, role) VALUES (?,?,?)",(customer['username'],customer['Password'],'customer'))
        self.cursor.execute("INSERT INTO customers VALUES (?, ?, ?, ?)", 
                            (customer['id'], customer['name'], customer['phone'], customer['email']))
        self.conn.commit()
        print("Customer registered successfully.")

    def view_customers(self):
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()
        print("\nCustomer List:")
        for customer in customers:
            print(customer)

    def view_bookings(self):
        self.cursor.execute("SELECT * FROM bookings")
        bookings = self.cursor.fetchall()
        print("\nBooking Details:")
        for booking in bookings:
            print(booking)

# Customer Interface
    def rent_car(self):
        self.cursor.execute("SELECT * FROM cars WHERE available=1")
        available_cars = self.cursor.fetchall()
        print("\nAvailable Cars:")
        for car in available_cars:
            print(car)

        car_id = input("Enter the ID of the car you want to rent: ")
        customer_id = input("Enter your customer ID: ")

        self.cursor.execute("SELECT * FROM cars WHERE id=? AND available=1", (car_id,))
        car = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM customers WHERE id=?", (customer_id,))
        customer = self.cursor.fetchone()

        if car and customer:
            days = int(input("Enter number of days to rent: "))
            total_rent = car[4] * days
            self.cursor.execute("INSERT INTO bookings (car_id, customer_id, days, total_rent) VALUES (?, ?, ?, ?)",
                                (car_id, customer_id, days, total_rent))
            self.cursor.execute("UPDATE cars SET available=0 WHERE id=?", (car_id,))
            self.conn.commit()
            print(f"Car rented successfully. Total rent: {total_rent}")
        else:
            print("Invalid car ID or customer ID.")

    def return_car(self):
        car_id = input("Enter the ID of the car you are returning: ")
        self.cursor.execute("SELECT * FROM cars WHERE id=? AND available=0", (car_id,))
        car = self.cursor.fetchone()

        if car:
            self.cursor.execute("UPDATE cars SET available=1 WHERE id=?", (car_id,))
            self.conn.commit()
            print("Car returned successfully.")
        else:
            print("Invalid car ID or car is not currently rented.")

    def run(self):
        while True:
            print("\n--- Car Rental System ---")
            print("1. Owner Interface")
            print("2. Employee Interface")
            print("3. Customer Interface")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                if self.login('owner'):
                    while True:
                        print("\n--- Owner Interface ---")
                        print("1. Add Car")
                        print("2. View Cars")
                        print("3. View Employees")
                        print("4. Add Employee")
                        print("5. Add Admin: ")
                        print("6. View Customers")
                        print("7. Remove car")
                        print("8. Remove employee")
                        print("9. Logout")
                        owner_choice = input("Enter your choice: ")

                        if owner_choice == '1':
                            self.add_car()
                        elif owner_choice == '2':
                            self.view_cars()
                        elif owner_choice == '3':
                            self.view_employees()
                        elif owner_choice == '4':
                            self.add_employee()
                        elif owner_choice=='5':
                            self.addadmin()
                        elif owner_choice == '6':
                            self.view_customers()
                        elif owner_choice == '7':
                            self.deletecar()
                        elif owner_choice=='8':
                            self.delemployee()
                        elif owner_choice=='9':
                            break

            elif choice == '2':
                if self.login('employee'):
                    while True:
                        print("\n--- Employee Interface ---")
                        
                        print("1. View Customers")
                        print("2. View Bookings")
                        print("3. Logout")
                        employee_choice = input("Enter your choice: ")

                        
                        if employee_choice == '1':
                            self.view_customers()
                        elif employee_choice == '2':
                            self.view_bookings()
                        
                        elif employee_choice == '3':
                            break

            elif choice == '3':
                print("Register if new Or Login into existing Account")
                c=input("1. Login\n2.Register")
                if c=='1': 
                    if self.login('customer'):
                        while True:
                            print("\n--- Customer Interface ---")
                            print("1. Rent Car")
                            print("2. Return Car")
                            print("3. Logout")
                            customer_choice = input("Enter your choice: ")

                            if customer_choice == '1':
                                self.rent_car()
                            elif customer_choice == '2':
                                self.return_car()
                            elif customer_choice == '3':
                                break
                elif c=='2':
                    print(" Register Customer")
                    self.register_customer()
                    

            elif choice == '4':
                print("Exiting system. Goodbye!")
                self.conn.close()
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    setup_database()
    system = CarRentalSystem()
    system.run()