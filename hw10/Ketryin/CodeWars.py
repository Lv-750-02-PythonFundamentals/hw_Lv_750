# Regular Ball Super Ball
class Ball(object):
	def __init__(self, ball_type='regular'):
		self.ball_type = ball_type
# Color Ghost
import random
class Ghost(object):
	def __init__(self):
		self.color = random.choice(['white', 'yellow', 'purple', 'red'])

# Classy Classes
class Person:
	def __init__(self, name,age):
		self.info=f"{name}s age is {age}"
		self.name=name
		self.age=int(age)
	@property
	def getInfo (self):
		return self.info

# Basic subclasses - Adam and Eve

class God():
	def __init__(self):
		self.humans = [Man("Adam"), Woman("Eve")]
	
	def __getitem__(self, i):
		return self.humans[i]
	
	def __len__(self):
		return len(self.humans)

class Human:
	def __init__(self, name):
		self.name = name

class Man(Human):
	def __init__(self, name):
		super().__init__(name)

class Woman(Human):
	def __init__(self, name):
		super().__init__(name)

# Building Spheres
import math
class Sphere(object):
	def __init__(self, radius, mass):
		self.radius=radius
		self.mass=mass
	def get_radius(self):
		return self.radius
	def get_mass(self):
		return self.mass
	def get_volume(self):
		return round(4/3*math.pi*self.radius**3, 5)
	def get_surface_area(self):
		return round(4*math.pi*self.radius**2, 5)  
	def get_density(self):
		return round(self.mass/(4/3*math.pi*self.radius**3), 5)
	
# Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError()

    cls.__name__ = new_name