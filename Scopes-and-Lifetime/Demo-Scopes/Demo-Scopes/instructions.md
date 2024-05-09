## **Scopes**

### **1. : Global Scope**
```python
global_var = "I am global_var"

def function_a():
  print(global_var) # Accessible as it is global

print(global_var) # Accessible as it is global
```

- **Global Scope**: A variable created in the main body of the Python code. The variable can be accessed/referenced from anywhere.

### **2. : Local Scope**
```python
def function_a():
  variable_a = "This is variable_a"
  print(variable_a) # Accessible as it is local
  
def function_b():
  print(variable_a) # NOT accessible as it is not local to function_b

print(variable_a) # NOT accessible as it is not global
```

- **Local Scope**: A variable created within the body of a function. The variable can be accessed/referenced from only within the function itself.

### **3. : Enclosing Scope**
```python
def outer():
  outer_var = "I am outer_var"
  def inner():
    print(outer_var) # Accessible as it is enclosed 
  
  inner()
  print(outer_var) # Accessible as it is local

print(variable_a) # NOT accessible as it is not global
```

- **Enclosing Scope**: A local scope of an outer function is the enclosing scope of an inner function. The variable can be accessed/referenced from the inner nested function.

