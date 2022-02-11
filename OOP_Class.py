# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:03:07 2021

@author: vajok
"""
"""
Creating a class with constructor that initialises

"""
class Dog:
    def __init__(self, name, age):         
        self.name = name
        self.age = age
        
        """
        description
        """
    def __str__(self):
        return f"{self.name} is {self.age} years old"
        
        
"""
Object creation
"""

a = Dog("S1",7)
b = Dog("S2",8)
print(a == b)

print(a.name)    

print(b.age)

mydog = Dog("Mdg", 4)
print(mydog)
print(a)
"""
__init__() and __str__() are called dunder methods because they begin and end with double underscores

""" 

print(isinstance(a, Dog))
