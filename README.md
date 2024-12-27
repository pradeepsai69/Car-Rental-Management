# Car-Rental-Management
This repository contains a Python-based Car Rental Management System, designed to manage a car rental business effectively. The system provides separate interfaces for Owners, Employees, and Customers, each with specific functionalities.

Features
Owner Interface
Add Admin: Owners can create additional admin accounts for managing the system.
Add Cars: Add new cars to the rental inventory, specifying details such as car ID, make, model, year, rent per day, and availability.
View Cars: Display a list of all cars in the inventory.
View Employees: Display all registered employees.
Add Employee: Add new employees to the system, including their username and password for login.
View Customers: Display a list of all registered customers.
Remove Car: Delete a car from the inventory using its ID.
Remove Employee: Delete an employee's account using their ID.
Logout: Exit the Owner Interface.
Employee Interface
View Customers: Display a list of all registered customers.
View Bookings: View details of all car bookings made by customers.
Logout: Exit the Employee Interface.
Customer Interface
Register Customer: Allows new customers to register by providing basic details like name, phone number, email, username, and password.
Rent Car: Rent a car by selecting from available cars, specifying the rental duration, and calculating the total cost.
Return Car: Return a rented car, making it available for others to rent.
Logout: Exit the Customer Interface.
System Overview
The system uses SQLite as the database for storing information about users, cars, employees, customers, and bookings. The system ensures:

Secure login for owners, employees, and customers based on roles.
Proper record-keeping with functionality for adding, viewing, updating, and deleting records.
How to Use
Database Setup:

Before running the system, ensure the database is initialized by calling the setup_database() function.
Run the System:

Execute the script to start the system. Users can select their role (Owner, Employee, Customer) and access relevant functionalities.
Interactivity:

The system features a console-based menu for seamless interaction with users.
Technologies Used
Python: Core programming language for developing the system.
SQLite: Lightweight database to store user, car, and booking information.
Directory Structure
db_setup.py: Contains the logic to initialize and set up the SQLite database.
main.py: The main script containing the CarRentalSystem class and the execution logic.
Example Scenarios
Owner adds a new car to the inventory, registers an employee, and views all customers.
Employee views the booking history and customer list.
Customer registers, rents a car, and returns it after usage.
Future Enhancements
GUI Implementation: Adding a graphical interface for improved usability.
Advanced Reports: Generate detailed reports for revenue, booking trends, and customer activity.
Payment Integration: Support for online payments.
Notifications: Email or SMS notifications for booking confirmation or return reminders.
This system serves as a robust foundation for managing car rental businesses with streamlined workflows and clear role-based functionalities.
