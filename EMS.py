employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Anjali', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Ravi', 'age': 25, 'department': 'IT', 'salary': 55000}
}

def add_employee():
    print("\n--- Add New Employee ---")
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employees:
        print("Employee ID already exists. Please use a unique ID.")
        return
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary (₹): "))
    employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
    print(f"Employee '{name}' added successfully!\n")

def view_employees():
    print("\n--- Employee List ---")
    if not employees:
        print("No employees available.\n")
        return
    print("{:<10} {:<15} {:<10} {:<15} {:<10}".format("ID", "Name", "Age", "Department", "Salary (₹)"))
    print("-" * 60)
    for emp_id, details in employees.items():
        print("{:<10} {:<15} {:<10} {:<15} {:<10}".format(
            emp_id, details['name'], details['age'], details['department'], details['salary']
        ))
    print()

def search_employee():
    print("\n--- Search Employee ---")
    emp_id = int(input("Enter Employee ID to search: "))
    if emp_id in employees:
        emp = employees[emp_id]
        print(f"\nEmployee Found!\nID: {emp_id}")
        print(f"Name: {emp['name']}")
        print(f"Age: {emp['age']}")
        print(f"Department: {emp['department']}")
        print(f"Salary: ₹{emp['salary']}\n")
    else:
        print("Employee not found.\n")

def main_menu():
    while True:
        print("========== EMPLOYEE MANAGEMENT SYSTEM ==========")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("\nThank you for using the Employee Management System. Goodbye!\n")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main_menu()
