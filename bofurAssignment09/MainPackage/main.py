'''
Name: Matthew Cox, Isaac Hedges, John O'connell, Spiros Yotas
email: cox2mr@ucmail.uc.edu, hedgesic@mail.uc.edu, oconnejh@mail.uc.edu, yotassg@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: We are modeling a shoe. This is the main
Citations:
Anything else that's relevant: 
'''
# Example Class
from ExamplePackage.ExampleClass import *
# Call dunder methods
example=Example(10)
print(Example.__repr__(example))
print(Example.__str__(example))
# Call get & set
Example.get(example)
Example.set(example,20)
# Call unique method of Class
Example.whatisvariabletype(example)