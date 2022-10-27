'''
Name: Matthew Cox, Isaac Hedges, John O'connell, Spiros Yotas
email: cox2mr@ucmail.uc.edu, hedgesic@mail.uc.edu, oconnejh@mail.uc.edu, yotassg@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: We are modelling a shoe. This is SoundbarClass
Citations:
Anything else that's relevant: 
'''
class SoundBar(): # New Sound Bar class
    # create new methods and store them
    def __init__(self, Volume):
        self.Volume = Volume 
        print("Successfully instantiated")
        
    def __repr__(self):
        '''
        return a string representation of the object
        '''
        return "Volume = " + str(self.Volume)
    
    def __str__(self):
        '''
        return a 'pretty' string representation of the object
        '''
        return "Volume = " + str(self.Volume)
    
    def get(self):
        return self.Volume
    
    def set(self, NewVolume):
        try:
            self.Volume = NewVolume
            print("Successfully set Volume as "+str(NewVolume))
            return True
        except:
            print("Failed to set Volume as "+str(NewVolume))
            return False
        
    def isLoudEnough(self,NewVolume):
        if NewVolume > 100:          
            print("Maximum Volume")
        else:
            self.Volume = NewVolume  