'''
Name: Matthew Cox, Isaac Hedges, John O'connell, Spiros Yotas
email: cox2mr@ucmail.uc.edu, heddgesic@mail.uc.edu, oconnejh@mail.uc.edu, yotassg@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: We are modelling a shoe. This is ShoeClass
Citations:
Anything else that's relevant: 
'''
class Example():
    def __init__(self,variable):
        self.variable=variable
        print("Successfully instantiated")
    def __repr__(self):
        '''
        return a string representation of the object.
        '''
        return "variable = "+str(self.variable)
    def __str__(self):
        '''
        return a 'pretty' string representation of the object
        '''
        return str(self.variable)+" is the variable in this example"
    def get(self):
        return self.variable
    def set(self,newvariable):
        try:
            self.variable=newvariable
            print("Successfully set variable as "+str(newvariable))
            return True
        except:
            print("Failed to set brand as "+str(newvariable))
            return False
    def whatisvariabletype(self):
        print(type(self.variable))