'''
Name: Matthew Cox, Isaac Hedges, John O'connell, Spiros Yotas
email: cox2mr@ucmail.uc.edu, heddgesic@mail.uc.edu, oconnejh@mail.uc.edu, yotassg@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: We are modeling a movie. This is MovieClass
Citations:
Anything else that's relevant: 
'''
class Movie():
    def __init__(self, title):
        self.title = title
        print("Successfully instantiated")
    def __repr__(self):
        '''
        return a string representation of the object.
        '''
        return "Movie = "+str(self.title)
    def __str__(self):
        '''
        return a 'pretty' string representation of the object
        '''
        return "Movie is set as " + self.title
    def get(self):
        return self.title
    def set(self,newTitle):
        try:
            self.title=newTitle
            print("Successfully set new movie as "+str(newTitle))
            return True
        except:
            print("Failed to set new movie as "+str(newTitle))
            return False
    def titleOfTheYear(self, proposedTitle):
        if proposedTitle=="Shrek":
            print("Shrek is the title of the year")
        else:
            print(str(proposedTitle)+ " is not the title of the year, Shrek is") 