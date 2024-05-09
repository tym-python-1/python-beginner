## **Loops and Iteration in Python**

### **1. While Loops:**
In Python, `while` loops are used to repeatedly execute a block of code as long as the condition is `True`. It's essential to modify the variable being evaluated in the condition inside the loop to avoid infinite loops.

```python
print("Let's print all integers smaller than or equal to the given number but greater than 0")
number = int(input("Give me a number "))
while number > 0:  
    print(number)  # Prints the current number
    number -= 1  # Decrements the number to avoid infinite loop
```
- This part prints all the integers from the given number to 1 in descending order.

### **2. Filtering in While Loops:**
While loops can also be used to filter and print specific numbers within a range or a condition, such as printing all even numbers below a given number.

```python
print("Let's print all even integers smaller than or equal to the given number but greater than 0")
number2 = int(input("Give me a number "))
while number2 > 0:
    if number2 % 2 == 0:
        print(number2)  # Prints the number if it is even
    number2 -= 1  # Decrements the number to avoid infinite loop
```
- This part prints all the even numbers from the given number down to 2, inclusive.

### **3. Loop Control Statements in While Loops:**
Just like in `for` loops, `break` and `continue` statements can be used in \`while\` loops to control the flow of execution.

```python
number3 = 10
while number3 > 0:
    if number3 == 5:
        break  # Will exit the loop when number3 is 5
    print(number3)  
    number3 -= 1
```

```python
number4 = 10
while number4 > 0:
    number4 -= 1
    if number4 % 2 != 0:
        continue  # Will skip the print statement if number4 is odd
    print(number4)
```

### **Note:**
- Ensure that the condition in a `while` loop eventually becomes `False` to avoid infinite loops.
- Use `break` to exit a `while` loop prematurely and `continue` to skip to the next iteration of the loop.
- Always be cautious when dealing with `while` loops to prevent unexpected behaviors in your program.
