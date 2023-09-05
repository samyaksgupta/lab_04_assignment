class Employee:
    def __init__(self, emp_id, name, age, sal):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.sal = sal

class Employeedbs:
    def __init__(self):
        self.emp = []

    def addEmp(self, emp):
        self.emp.append(emp)

    def search_by_age(self, age):
        result = [emp for emp in self.emp if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.emp if emp.name.lower() == name.lower()]
        return result

    def search_by_sal(self, operation, sal):
        if operation == '>':
            result = [emp for emp in self.emp if emp.sal > sal]
        elif operation == '<':
            result = [emp for emp in self.emp if emp.sal < sal]
        elif operation == '>=':
            result = [emp for emp in self.emp if emp.sal >= sal]
        elif operation == '<=':
            result = [emp for emp in self.emp if emp.sal <= sal]
        else:
            result = []
        return result

def main():
    dbs = Employeedbs()

    # Add emp to the dbs
    emp1 = Employee("161E90", "Raman", 41, 56000)
    emp2 = Employee("161F91", "Himadri", 38, 67500)
    emp3 = Employee("161F99", "Jaya", 51, 82100)
    emp4 = Employee("171E20", "Tejas", 30, 55000)
    emp5 = Employee("171G30", "Ajay", 45, 44000)

    dbs.addEmp(emp1)
    dbs.addEmp(emp2)
    dbs.addEmp(emp3)
    dbs.addEmp(emp4)
    dbs.addEmp(emp5)

    while True:
        print("\nSearch options:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by sal")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            age = int(input("Enter age to search: "))
            result = dbs.search_by_age(age)
        elif choice == 2:
            name = input("Enter name to search: ")
            result = dbs.search_by_name(name)
        elif choice == 3:
            operation = input("Enter operation (>, <, >=, <=): ")
            sal = float(input("Enter Salary to search: "))
            result = dbs.search_by_sal(operation, sal)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if not result:
            print("No matching records found.")
        else:
            print("\nMatching records:")
            for emp in result:
                print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, sal: {emp.sal}")
                print("Samyak Sanjiv Gupta E22CSEU1090" )

if __name__ == "__main__":
    main()
