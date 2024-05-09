## **Loops and Iteration in Python**

### **1. Iterating through Lists:**
```python
fruits = ['Apple', 'Orange', 'Banana']
for fruit in fruits:
    print(fruit)  # Prints each fruit in the list, one by one
    print(fruit + " Pie")  # Prints each fruit followed by " Pie"
```

- You can execute any kind of statements inside the loop, including conditionals.

```python
numbers = [4, 7, 2, 5, 33, 9, 4]
for number in numbers:
    if number % 2 == 0:
        print('Even')  # Prints 'Even' if the number is even
    else:
        print('Odd')  # Prints 'Odd' if the number is odd
```

### **2. Using `range()` Function:**
```python
for number in range(11):  # Prints numbers from 0 to 10
    print(number)
for number in range(5, 21, 2):  # Prints numbers from 5 to 20 with a step of 2
    print(number)
```

### **3. Control Statements in Loops:**

- **`break` Statement:**
```python
numbers = [4, 6, 11, 8, 12]
for number in numbers:
    if number > 10:
        print(number)  # Prints the number if it's greater than 10
        break  # Exits the loop as soon as a number greater than 10 is found
```

- **`continue` Statement:**
```python
numbers = [4, 6, 11, 8, 12]
for number in numbers:
    if number >= 10:
        continue  # Skips the current iteration if number is 10 or greater
    print(number + 2)  # Adds 2 to the number and prints it, if number is less than 10
```

### **Note:**
- The `range()` function can take one (stop), two (start, stop), or three (start, stop, step) arguments.
- The `break` statement is used to exit a for loop prematurely.
- The `continue` statement is used to skip the current iteration of the loop and continue with the next one.
