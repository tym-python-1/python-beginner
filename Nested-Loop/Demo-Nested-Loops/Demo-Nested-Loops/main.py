## Lets learn about nested loops!!

### First lets try to create some fun patterns with nested loops ##
print("\n---- Example 1 ----")

for row in range(5): # Change range to increase the width of the pattern
  for column in range(7): # Change range to increase the height of the pattern
    # Try removing end="" to see what happens
    print("*", end="") # end="" allows us to tell python to not go to the next line
  print() # Implicitly goes to the next line


### We can create interesting shapes like a diagonal line!
print("\n---- Example 2 ----")

for row in range(5):
  for column in range(5):
    if(row == column):
      print("*", end="")
    else:
      print(" ", end="") # print 1 blank space
  print() # Implicitly goes to the next line

### We can create interesting shapes like a diagonal line!
print("\n---- Example 3 ----")

for i in range(5, 0, -1):
  for j in range(0, i):
      print("*", end="")  # Prints an asterisk and a space without moving to a new line
  print("")  # Moves to the next line


### What about number patterns
print("\n---- Example 4 ----")

for row in range(1, 5):
  for column in range(row):
    print(row, end="")
  print() # Implicitly goes to the next line




################################################
#### Optional Demos (We will go more into this in the future)####

##### We can concatenate each name in the list with each message in the list
print("\n---- Optional Example 1 ----")
names = ["John", "Ashley", "Brian"]
messages = ["is Happy.", "love dogs!", "love cats too!"]
for name in names:
  for message in messages:
    print(name, message)

##### We can also make each person shake hands only once
print("\n---- Optional Example 2 ----")
number_of_people = len(names)
for index1 in range(number_of_people):
  for index2 in range(index1, number_of_people): # start index1, to prevent double hand shaking
    print(names[index1], "shakes hands with", names[index2])
    
  


