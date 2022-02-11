# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:28:01 2021

@author: vajok
"""


# Illustration of multi-level inheritance

class Marks:                    #Base Class
    "This is a marks class that takes care of the marks data"

    def __init__(self):
        self.m1 = int(input("Enter marks in Physics: "))
        self.m2 = int(input("Enter marks in Chemistry: "))
        self.m3 = int(input("Enter marks in Maths: "))

    def displayMarks(self):
        print("Marks in Physics: ", self.m1)
        print("Marks in Chemistry: ", self.m2)
        print("Marks in Maths: ", self.m3)

class Result(Marks): #Derived class 
    "This is a result class that takes care of the result"

    def __init__(self):
        super( ).__init__( )
        self.total = self.m1 + self.m2 + self.m3
        self.percentage = self.total/3

    def displayResult(self):
        print("Total Marks: ", self.total)
        print("Percentage: ", self.percentage)

#(multi-level inheritance)
class Grade(Result): #Derived class 
    "This is a grade class that takes care of the grades"

    def __init__(self):     
        super( ).__init__( )
        if self.percentage > 80:
            self.grade = "A"
        elif self.percentage > 60:
            self.grade = "B"
        elif self.percentage > 40:
            self.grade = "C"
        else:
            self.grade = "Fail"

    def displayGrade(self):
        print("Grade: ", self.grade)
        
#Creating object of the derived class
g = Grade( )   
#Accessing the functions of all 
#parent classes using the object of last child class                 
g.displayMarks( )           
g.displayResult( )
g.displayGrade( )
