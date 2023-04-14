# Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type


# Color Ghost
class Ghost(object):
    colors = ["white", "yellow", "purple", "red"]
    id = -1
    def __init__(self):
        if Ghost.id == 3:
            Ghost.id = -1
        Ghost.id += 1
        self.color = Ghost.colors[Ghost.id]


# Basic subclasses - Adam and Eve
def God():
    man = Man()
    woman = Woman()
    return [man, woman]

class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


# Classy Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info= f"{name}s age is {age}"


# Building Spheres
from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(4 / 3 * pi * self.radius**3, 5)
    
    def get_surface_area(self):
        return round(4 * pi * self.radius**2, 5)
        
    def get_density(self):
        return round(self.mass / (4 / 3 * pi * self.radius**3), 5)
    

# Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    cls.__name__ = new_name if new_name.isalnum() and new_name[0] == new_name[0].upper() and new_name[0].isalpha() else None