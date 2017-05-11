from battery import Battery

class Car:
	"""A Simple Car class"""
	def __init__(self, make, model, year):
		"""Construction function"""
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name


class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

audi_a4 = ElectricCar('audi', 'a4', 2016)

print( audi_a4.get_descriptive_name() )
audi_a4.battery.describe_battery()
