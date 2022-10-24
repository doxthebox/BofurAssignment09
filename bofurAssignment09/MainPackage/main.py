'''
Name: Matthew Cox, Isaac Hedges, John O'connell, Spiros Yotas
email: cox2mr@ucmail.uc.edu, heddgesic@mail.uc.edu, oconnejh@mail.uc.edu, yotassg@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: We are modelling a shoe. This is the main
Citations:
Anything else that's relevant: 
'''
from ShoePackage.ShoeClass import *
# instantiate at least one object
shoe=Shoe("Size","Style","Brand")
# Invoke the dunder and non dunder methods
print(Shoe.__repr__(shoe))
print(Shoe.__str__(shoe))