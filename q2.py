class Company:
    def __init__(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

    def display_c(self):
        print("Company Name:", self.name)
        print("City:", self.city)
        print("Mobile No:", self.mobile_no)


class Employee(Company):
    def __init__(self, name, city, mobile_no, emp_name, designation, salary):
        super().__init__(name, city, mobile_no)
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

    def display_e(self):
        print("Employee Name:", self.emp_name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

emp = Employee("ABC Corporation", "rajkot", "9999999999", "dharmesh", "Software Engineer", 50000)

print("Company Details:")
emp.display_c()
print()

print("Employee Details:")
emp.display_e()