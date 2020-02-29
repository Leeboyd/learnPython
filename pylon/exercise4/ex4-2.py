import classes.PayrollSystem as HR
import classes.Employee as Employee
import classes.DisgruntledEmployee as Disgruntled

salary_employee = Employee.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = Employee.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = Employee.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
disgruntled_employee = Disgruntled.DisgruntledEmployee(20000, 'Anonymous')
payroll_system = HR.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee,
    disgruntled_employee
])