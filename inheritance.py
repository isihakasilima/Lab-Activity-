class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def calculate_pay(self):
		return self.salary

class Manager(Employee):
	def __init__(self, name, salary, bonus):
		super().__init__(name, salary)
		self.bonus = bonus

	def calculate_pay(self):
		return self.salary + self.bonus

#testing my code

e1 = Employee("Ali", 500000)
m1 = Manager("Juma", 500000, 150000)

print( e1.calculate_pay())
print( m1.calculate_pay())
