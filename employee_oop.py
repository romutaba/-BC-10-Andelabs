#class that implements employees attributes, supervisors 
import datetime 

class Employee(object):

	number_of_employees = 0   
	raise_amount = 1.03

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		Employee.number_of_employees += 1
	#method that determines employees full name
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	#method to increase salary
	def raise_sal(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod #allows user to pass an employee string in the format (firstnam-lastname-salary)
	def from_string(cls, employee_str):
		first, last, pay = employee_str.split('-')
		return cls(first, last, pay)
	#method for determining if it is a work day
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() ==6:
			return False
		return True


class Developer(Employee):

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		#initialize employees to an empty list
		if employees is None:
		 	self.employees = []
		else:
		 	self.employees = employees
	#method to add employee
	def add_employee(self, employee):
		if employee not in self.employees:
			self.employees.append(employee)
	#method to remove employee
	def remove_employee(self, employee):
		if employee in self.employees:
			self.employees.remove(employee)
	#method to print employees from list
	def print_employees(self):
		for employee in self.employees:
			print('--', employee.fullname())