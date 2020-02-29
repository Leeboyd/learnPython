import classes.PayrollSystem as HR
import classes.Employee as Employee

salary_employee = Employee.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = Employee.HourlyEmployee(2, 'John Wick', 40, 15)
commission_employee = Employee.CommissionEmployee(3, 'Kevin', 1000, 250)

payroll_system = HR.PayrollSystem()
payroll_system.calculate_payroll([
  salary_employee,
  hourly_employee,
  commission_employee
])