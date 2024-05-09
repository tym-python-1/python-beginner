# We can use import keyword to import modules into our file
# If you look to the left panel, you see that we are in the main file main.py 
# .py is an extension which denotes that the file is a python file
import math
import random
import requests
# import statements are always located at the top of the file
from constants import cat_image, dog_image, greetings

############################################## math module ##############################################
#                      The math module provides a range of constants and functions                      #
#                             that are related to mathematical operation                                #
#########################################################################################################

# Getting constants from the math module
print(math.pi)

# Using functions that are part of the math module

# math.factorial(): function returns the factorial of the number passed in as input
#                   factorial(1) is 1! which is 1
#                   factorial(2) is 2! which is 2 x 1 = 2   
#                   factorial(3) is 3! which is 3 x 2 x 1 = 6         
#                   factorial(4) is 4! which is 4 x 3 x 2 x 1 = 24   
print(math.factorial(4))


# math.ceil(): Rounds the number UP to the nearest whole number
print(math.ceil(4.3))

# math.floor(): Rounds the number DOWN to the nearest whole number
print(math.floor(4.3))

# math.pow(): Returns the result of a number raised to another number
# pow(2, 3) refers to 2 raised to the power of 3 which is 2 x 2 x 2 = 8
print(math.pow(2, 3))

# pow(3, 4) refers to 3 raised to the power of 4 which is 3 x 3 x 3 x 3 = 81
print(math.pow(3, 4))


############################################# random module #############################################
#                      The random module provides a range of constants and functions                    #
#                             that helps to generate random numbers                                     #
#########################################################################################################

# This generates a random number between 0 to 10
print(random.randrange(10))

############################################# random module #############################################
#                      The requests module allows you to send HTTP requests using Python                #
#                                  this topic is out of scope for our lesson                            #
#########################################################################################################


############################################# random module #############################################
#                      We can import constants and functions we created from other files                #
#########################################################################################################
print(cat_image)
print(dog_image)
greetings("John")