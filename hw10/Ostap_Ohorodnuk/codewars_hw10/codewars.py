#task1_________________________________

class Ball(object):
	"""boll super boll"""
	def __init__(self, ball_type='regular'):
		self.ball_type = ball_type
# task2_________________________________


import random
class Ghost(object):
	""""Color Ghost"""
	def __init__(self):
		self.color = random.choice(['white', 'yellow', 'purple', 'red'])


#task 3_________________________________
def God():
    return [ Man("Adam"), Woman("Eva") ]

class Human:
   def __init__( self, name ):
      self.name = name

class Man( Human ):
   def __init__( self, name ):
      self.name = name

class Woman( Human ):
   def __init__( self, name ):
      self.name = name



#task 4_________________________________

class Person:
    """Classy Classes"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return "{0.name}s age is {0.age}".format(self)

#task 5_________________________________
import math

class Sphere:
    """Building Spheres"""
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4 / 3) * math.pi * (self.radius ** 3), 5)

    def get_surface_area(self):
        return round(4 * math.pi * (self.radius ** 2), 5)

    def get_density(self):
        return round(self.mass / ((4 / 3) * math.pi * (self.radius ** 3)), 5)
#task 6_________________________________

def class_name_changer(cls, new_name):
    """Python's Dynamic Classes #1"""
    if not new_name or not new_name[0].isupper() or not new_name.isalnum():
    	raise ValueError()
    cls.__name__ = new_name