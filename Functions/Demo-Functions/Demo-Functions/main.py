print("----- Example #1 -----")
# Example #1: Function to ask user for two numbers
#             and print the sum of the two numbers
def sum_two_numbers():
  # These two variables are defined inside the scope of the function
  print("Summing two numbers")
  number1 = int(input("Please input the first number: "))
  number2 = int(input("Please input the second number: "))
  sum = number1 + number2
  print(f"Sum of two numbers is {sum}" )

sum_two_numbers()

#################################################
print("\n----- Example #2 -----")
# Example #2 Returning a value
def say_hello():
  return "Hello there" # Return allow us to send back the result

message = say_hello()
print("The message says:", message)

#################################################
print("\n----- Example #3 -----")
# Example #3 Greeting the user
def greet():
  user = input("Hi! What is your name: ")
  print("Hello", user)

## After creating a function we can run it by simply calling the greet function!

## For instance, lets say we want to greet 3 different users!
greet()
greet()
greet()

print("\n----- Example #3 Error Example -----")
print("We will receive an error below because the user variable inside of the greet() function is not defined outside of the function")
print("All variable inside of a function is only recognise inside of the function! :)")
# Comment the line below to remove error
print(user)


