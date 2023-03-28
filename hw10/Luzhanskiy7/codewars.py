# Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


ball1 = Ball()
ball2 = Ball('super')

# Color Ghost
import random


class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)


ghost = Ghost()
print(ghost.color)

# Basic subclasses - Adam and Eve
class Human():
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]

# Classy Classe
class Person():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def getInfo(self):
        return f'{self.name}s age is {self.age}'


person = Person('john', 16)
print(person.getInfo())

# Building Spheres
import math as m


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        self.vol = 4 / 3 * m.pi * self.radius ** 3
        return round(self.vol, 5)

    def get_surface_area(self):
        area = 4 * m.pi * self.radius ** 2
        return round(area, 5)

    def get_density(self):
        d = self.mass / self.vol
        return round(d, 5)


ball = Sphere(2, 50)
ball.get_radius()
ball.get_mass()
ball.get_volume()
ball.get_surface_area()
ball.get_density()



