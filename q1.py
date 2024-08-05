from datetime import datetime

class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = datetime.strptime(date_of_join, "%d-%m-%Y")
        self.designation = designation
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Date of Join:", self.date_of_join.strftime("%d-%m-%Y"))
        print("Designation:", self.designation)
        print("Salary:", self.salary)

emp1 = Employee("dharmesh", "01-01-2020", "Software Engineer", 50000)
emp2 = Employee("jayesh", "15-06-2018", "Manager", 80000)

print("Employee 1 Details:")
emp1.display_details()
print()

print("Employee 2 Details:")
emp2.display_details()
