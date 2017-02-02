class Animal:
	def __init__(self, name):
		self.name = name

	def talk(self):
		pass



pet_qazi = Animal("QAZI")
print(pet_qazi.name)

class Dog(Animal): # Inherits from the class Animal above.
	def talk(self):
		return "Woof"

pet = Dog("Dot")
print(pet.name)
print(pet.talk())



