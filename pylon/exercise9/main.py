import json

from classes.Employee import employee_database, Employee
from classes.Productivity import track
from classes.HR import calculate_payroll

def print_dict(d):
  print(json.dumps(d, indent=2))

employees = employee_database.employees
track(employees, 40)
calculate_payroll(employees)

for employee in employees:
  # print(employee.__dict__)
  print(employee.to_dict())

temp_secretary = Employee(5)
print('Temporary Secretary:')
print_dict(temp_secretary.to_dict())