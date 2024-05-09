print("Hello, world! This is Python 3!")
# Print given number to 1 in descending order
# print("Let's print all integers smaller than or equal to the given number but greater than 0")
# number = int(input("Give me a number "))
# while( number > 0):
#   print(number)
#   # In a while loop, if the condition is true,
#   # it will keep executing the code inside the loop
#   # To get out of the loop, we must make sure that the
#   # condition eventually is not satisfied (false)
#   # In this example, we can do so by subtracting 1 from
#   # the given number each time we print it
#   number -= 1
# print()

# Print all even numbers below given number2
print("Let's print all even integers smaller than or equal to the given number but greater than 0")
number2 = int(input("Give me a number "))

while (number2 > 0):
  if number2 % 2 == 0:
    print(number2)
  number2 -= 1
print("Stop")

