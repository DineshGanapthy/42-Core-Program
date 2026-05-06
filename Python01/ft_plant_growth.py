class Plant:
	def __init__(self, name: str, height: int, age: int) -> None: # water: int, weather: str
		"""Initialize a Plant instance."""
		self.name = name 
		self.height = height
		self.age_days = age
		#self.water = water
		#self.weather = weather
	
	def show(self) -> None:
		"""Print/Show the plant information"""
		print(f"{self.name}: {self.height}cm, {self.age_days} days old")

	def grow(self) -> None:
		"""Increase the height by 0.8cm for each condition"""
		#if (self.weather = "Sunlight")
		self.height += 0.8
		#if (self.water <= 2)
		#	self.height += 0.4

	def age(self) -> None:
		"""Increase the age by 1 day"""
		self.age_days += 1

def ft_garden_growth() -> None:
	"""Create and display a registry of garden Plants."""

	current_day = 1
	plants = [ Plant("Rose", 25, 30), ]
	#Plant("Sunflower", 80, 45),
	#Plant("Cactus", 15, 120),

	print("=== Garden Plant Growth ===")
	for plant in plants:
		plant.grow()
	
	while (current_day < 7):
		print(f"=== Day {current_day} ===")
		for plant in plants:
			plant.grow()
			plant.age()
			plant.show()
		current_day += 1


if __name__ == "__main__":
	ft_garden_growth()