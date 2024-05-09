## **Functions**

### **1. Addition function:**
We can create a function that allows us to run a sequence anytime simply by calling the function name.

```python
def sum_two_numbers():
  # These two variables are defined inside the scope of the function
  print("Summing two numbers")
  number1 = int(input("Please input the first number: "))
  number2 = int(input("Please input the second number: "))
  sum = number1 + number2
  print(f"Sum of two numbers is {sum}" )

sum_two_numbers()
```

### **2. Return keyword:**
We can use the `return` keyword to send back the result of a function. Return does not print the value to output.

```python
def say_hello():
  return "Hello there" # Return allow us to send back the result

message = say_hello()
print("The message says:", message)
```

### **3. Greet function:**
We can call a function multiple times.

```python
def greet():
  user = input("Hi! What is your name: ")
  print("Hello", user)

## After creating a function we can run it by simply calling the greet function!

## For instance, lets say we want to greet 3 different users!
greet()
greet()
greet()
```

### **4. Scopes**
If we try to obtain a variable from a function, we will receive an error since the variable only exist inside of the function.

```python
print("We will receive an error below because the user variable inside of the greet() function is not defined outside of the function")
print("All variable inside of a function is only recognise inside of the function! :)")
# Comment the line below to remove error
print(user)
```

- **Scope:** Variables inside a function are in local scope, those outside are in global scope.
- **Returning Values:** Using the `return` keyword to send back results.

