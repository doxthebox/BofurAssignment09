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
class Shoe():
    def __init__(self,size,style,brand):
        if self.validatesize(size)==True:
            if self.validatebrand(brand)==True:
                if self.validatestyle(style):
                    self.size=size
                    self.brand=brand
                    self.size=size
                    print("Successfully instantiated")
                else:
                    pass
            else:
                pass
        else:
            pass
    def __repr__(self):
        '''
        return a string representation of the object.
        '''
        return "style = "+str(self.style)+", brand = "+str(self.brand)+", size = "+str(self.size)
    def __str__(self):
        '''
        return a 'pretty' string representation of the object
        '''
        return str(self.size)+" shoe from "+str(self.brand)+" in the "+str(self.style)+" style"