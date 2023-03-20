# Task 1

class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Task 2
import random


class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "red", "purple"])


# Task 3

class God:
    def __init__(self):
        self.humans = [Man("Adam"), Woman("Eve")]

    def __getitem__(self, element):
        return self.humans[element]

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


# Task 4

class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"
        self.name = name
        self.age = int(age)

    @property
    def getInfo(self):
        return self.info


# Task 5

import math


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * math.pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 5)

    def get_density(self):
        return round(self.mass / (4 / 3 * math.pi * self.radius ** 3), 5)


# Task 6

def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError()

    cls.__name__ = new_name
