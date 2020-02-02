#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:43:47 2020

@author: fatimaal-hussein
"""


#%%  Exceptions
try:
    age = int(input('Age:  '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value')

#%% Classes
    
class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

#%% Constructors (construct or create an object)  def __init__(self, name):

    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")


point = Point(10,20)
print(point.x)

#%% person  - name attr talk()

class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi, I am  {self.name}")
        
        
john = Person("John Smith")
john.talk()

bob = Person("bob smith")
bob.talk()
    
#%% example of constructors

class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi, I love you {self.name} ")

ali = Person("Ali")
ali.talk()


#%% Inheritance

class Mammal:
    def walk(self):
        print("walk")
        
        
class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")
    
    
cat1 = Cat()
cat1.walk()

#%% 





    