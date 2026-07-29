# Parent Class  --> part 1
class Employee:
    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Employee ID: {self.emp_id} | Name: {self.name} | Age: {self.age}")

    def calculate_salary(self):
        return 0


# Child Classes --> part 2
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, age, monthly_salary):
        super().__init__(emp_id, name, age)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, age, hourly_rate, hours_worked):
        super().__init__(emp_id, name, age)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Freelancer(Employee):
    def __init__(self, emp_id, name, age, project_rate, completed_projects):
        super().__init__(emp_id, name, age)
        self.project_rate = project_rate
        self.completed_projects = completed_projects

    def calculate_salary(self):
        return self.project_rate * self.completed_projects


# List --> part 3
employees = []

while True:
  print("\n--- Employee Entry ---")
  emp_type = input("Enter Type --> [1: FullTime, 2: PartTime, 3: Freelancer] or ['q'] to finish: ")

  if emp_type.lower() == "q":
    break

  emp_id = int(input("Enter ID: "))
  name = input("Enter Name: ")
  age = int(input("Enter Age: "))

  if emp_type == "1":
    salary = int(input("Enter Monthly Salary: "))
    employees.append(FullTimeEmployee(emp_id, name, age, salary))

  elif emp_type == "2":
    rate = int(input("Enter Hourly Rate: "))
    hours = int(input("Enter Hours Worked: "))
    employees.append(PartTimeEmployee(emp_id, name, age, rate, hours))

  elif emp_type == "3":
    rate = int(input("Enter Project Rate: "))
    projects = int(input("Enter Completed Projects: "))
    employees.append(Freelancer(emp_id, name, age, rate, projects))


print("\n--- Employee's Information ---")
for i in employees:
    i.display_info()
    print(f"Salary: {i.calculate_salary()} $")
    print("--------------------------")


# Employee Report --> part 4
print("\n--- Employee Report ---")

total_employees = len(employees)
print(f"Total Employees: {total_employees}")

if total_employees > 0:
  total_payroll = 0
  for i in employees:
    total_payroll += i.calculate_salary()

  highest_paid = employees[0]
  for i in employees:
    if i.calculate_salary() > highest_paid.calculate_salary():
      highest_paid = i

  print(f"Total Payroll: {total_payroll} $")
  print(f"Highest Paid Employee: {highest_paid.name} {highest_paid.calculate_salary()} $\n")
else:
  print("No employees entered.")