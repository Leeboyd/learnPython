from classes.HR import (
  PayrollSystem,
  SalaryPolicy,
  CommissionPolicy,
  HourlyPolicy 
)

from classes.Productivity import (
  ProductivitySystem,
  ManagerRole,
  SecretaryRole,
  SalesRole,
  FactoryRole
)

from classes.Contact import (
  AddressBook
)

from classes.Mixin import (
  AsDictionaryMixin
)

class EmployeeDatabase:
  def __init__(self):
    self._employees = [
      {
        'id': 1,
        'name': 'Mary Poppins',
        'role': 'manager'
      },
      {
        'id': 2,
        'name': 'John Smith',
        'role': 'secretary'
      },
      {
        'id': 3,
        'name': 'Kevin Bacon',
        'role': 'sales'
      },
      {
        'id': 4,
        'name': 'Jane Doe',
        'role': 'factory'
      },
      {
        'id': 5,
        'name': 'Robin Williams',
        'role': 'secretary'
      },
    ]
    self.productivity = ProductivitySystem()
    self.payroll = PayrollSystem()
    self.employee_addresses = AddressBook()

  @property
  def employees(self):
    return [self._create_employee(**data) for data in self._employees]

  def _create_employee(self, id, name, role):
    address = self.employee_addresses.get_employee_address(id)
    payroll_policy = self.payroll.get_policy(id)
    employ_role = self.productivity.get_role(role)
    return Employee(id, name, address, payroll_policy, employ_role)


class Employee(AsDictionaryMixin):
  def __init__(self, id, name, address, payroll_policy, employ_role):
    self.id = id
    self.name = name
    self.address = address
    self._payroll_policy = payroll_policy
    self._employ_role = employ_role
  
  def work(self, hours):
    duties = self._employ_role.perform_duties(hours)
    print(f'Employee {self.id} - {self.name}:')
    print(f'- {duties}')
    print('')
    self._payroll_policy.track_work(hours)
  
  def calculate_payroll(self):
    return self._payroll_policy.calculate_payroll()