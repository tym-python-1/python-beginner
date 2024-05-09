print("----- Example #1 -----")
# Example #1: Simple function to say Hello to a given name ###
def greetings(name):
  # Code to execute
  print("Hello " + name)

greetings("Tom")
greetings("Jane")

print("\n----- Example #2 -----")
# Example #2: Function to ask user for two numbers
#             and print the sum of the two numbers
def sum_two_numbers(number1, number2):
  sum = number1 + number2
  # We use return to send back values that we can store to use for later
  # If we print, it will output the value but we cannot store it
  return sum 

result_2 = sum_two_numbers(3,5)
print(result_2)

print("\n----- Example #3 -----")
### A function that substracts num1 by num2
def subtract(num1, num2):
  return num1 - num2

# We can also pass in variables as arguments
number1 = 12
number2 = 3

# We can call the function and set the result returned into a variable
result = subtract(number1, number2)
print("The result is", result)
