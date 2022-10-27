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
class TV(): # New TV class
    # create new methods and store them
    def __init__(self, Type):
        self.Type = Type 
        print("Successfully instantiated")
        
    def __repr__(self):
        '''
        return a string representation of the object
        '''
        return "Type = " + str(self.Type)
    
    def __str__(self):
        '''
        return a 'pretty' string representation of the object
        '''
        return "Type = " + self.Type
    
    def get(self):
        return self.Type
    
    def set(self, Price):
        try:
            self.Type=Price
            print("Successfully set variable as "+str(Price))
            return True
        except:
            print("Failed to set Type as "+str(Price))
            return False
        
    def isWithinBudget(self,Price):
        if Price > 1000:          
            print("Over Budget")
        else:
            self.Price = Price      