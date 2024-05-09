## **Nested Loops in Python**

### **1. Patterns with Nested Loops:**
In this example, we use two for loops to create a simple pattern of asterisks (*). The outer loop handles the number of rows, while the inner loop handles the number of columns.

```python
for row in range(5):
    for column in range(7): 
        print("*", end="")
    print()
```
- We can increase the size of the pattern by modifying the values in the range function.

### **2. Creating Lines with Nested Loops:**
In this example, we create a diagonal line using asterisks (*). The outer loop still handles the rows, inner loop handles the columns, and we added some conditions inside of the loop!.

```python
for row in range(5):
  for column in range(5):
    if(row == column):
      print("*", end="")
    else:
      print(" ", end="") # print 1 blank space
  print()
```
- If row = col then it must be a point a the diagonal line.

### **3. Creating Shapes with Nested Loops:**
In this example, the user provides the number of rows of the triangle. The outer loop starts at the number of rows and iterates backwards down to 1, while the inner loop runs for the current outer loop index number of times. The result is an inverted right-angled triangle.

```python
for i in range(5, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")  # Prints an asterisk and a space without moving to a new line
    print("\n")  # Moves to the next line
```

### **4. Number Patterns with Nested Loops:**
In this example, we create a number pattern where each row contains the row number repeated for the row number of times. For instance, row 3 contains '333'.

```python
for row in range(1, 5):
    for column in range(row):
        print(row, end="")
    print()  # Implicitly goes to the next line
```

### **Note:**
- The `end=""` in the print function is used to prevent moving to a new line after each print statement. By default, print moves to a new line.
- The `print()` without arguments implicitly moves to the next line, creating a new row for our patterns.
- We can nest `while`/`for` loops in any order.

## **Additional Demo**

### **1. Message combination**
We can concatenate each name in the list with each message in the list to print all possible permutation(combination). 

```python
names = ["John", "Ashley", "Brian"]
messages = ["is Happy.", "love dogs!", "love cats too!"]
for name in names:
  for message in messages:
    print(name, message)
```

- Every single person in the list is happy, loves dogs and love cats!

### **2. Shaking hands**
We will learn more about list in the future but you can see how nested loops can be used along with list!

```python
names = ["John", "Ashley", "Brian"]
messages = ["is Happy.", "love dogs!", "love cats too!"]
for name in names:
  for message in messages:
    print(name, message)
```

- We can also make each person shake hands with each other once, without any repeats
