import json

from classes.Employee import EmployeeDatabase
from classes.Productivity import ProductivitySystem
from classes.HR import PayrollSystem

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)

def print_dict(d):
  print(json.dumps(d, indent=2))

for employee in employees:
  # print(employee.__dict__)
  print(employee.to_dict())