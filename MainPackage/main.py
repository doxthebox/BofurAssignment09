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
# MovieClass
from MoviePackage.MovieClass import Movie
# Call dunder methods
examplemovie=Movie("Shrek")
print(Movie.__repr__(examplemovie))
print(Movie.__str__(examplemovie))
# Call get & set
Movie.get(examplemovie)
Movie.set(examplemovie,"Up")
# Call unique method of Class
Movie.titleOfTheYear(examplemovie,"Shrek")

# SoundBarClass
from SoundBarPackage.SoundBarClass import SoundBar
# Call dunder methods
examplesoundbar=SoundBar(20)
print(SoundBar.__repr__(examplesoundbar))
print(SoundBar.__str__(examplesoundbar))
# Call get & set
SoundBar.get(examplesoundbar)
SoundBar.set(examplesoundbar,100)
# Call unique method of Class
SoundBar.isLoudEnough(examplesoundbar,200)

# tvClass
from tvPackage.tvClass import TV
# Call dunder methods
exampletv=TV("Samsung")
print(TV.__repr__(exampletv))
print(TV.__str__(exampletv))
# Call set & get
TV.get(exampletv)
TV.set(exampletv,200)
# Call unique method of Class
TV.isWithinBudget(exampletv,1000)