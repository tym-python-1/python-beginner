## **Python Programming Concepts**

### **1. Functions:**
```python
def greetings(name):
  # Code to execute
  print("Hello " + name)

greetings("Tom")
greetings("Jane")
```

- **Scope:** Variables inside a function are in local scope, those outside are in global scope.
  


### **2. Return**
```python
def sum_two_numbers(number1, number2):
  sum = number1 + number2
  return sum 

result_2 = sum_two_numbers(3,5)
print(result_2)
```

- **Returning Values:** Using the `return` keyword to send back results. We can return and store these results to be used for later.

### **3. Arguments**

```python
def subtract(num1, num2):
  return num1 - num2

number1 = 12
number2 = 3

result = subtract(number1, number2)
print("The result is", result)
```

- We can also pass in variables as an argument.

### **Note:**
- Variables have scope, defining the region where they can be accessed or modified.
- Functions can be used to encapsulate and reuse code, and they can return values using the `return` keyword.
