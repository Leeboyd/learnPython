# import classes.Employee as employees
# import classes.Productivity as productivity
# import classes.HR as hr

from classes.Employee import EmployeeDatabase
from classes.Productivity import ProductivitySystem
from classes.HR import PayrollSystem

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)