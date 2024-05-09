## Global Scope Example
### Global scoped variable can be access/referenced from anywhere. Hence, the name Global.
global_var = "I am global_var"

def main():
  function_a()
  function_b()
  outer()

## Local Scope Example
### Local scoped variable can be access/referenced from only within the function. Hence, the variable is only recognise locally in the function.
def function_a():
  variable_a = "This is variable_a"
  # Uncomment the code below to try to access variable a
  # print(variable_a)
  print(global_var)
  
def function_b():
  # Uncomment the code below to try to access variable a
  # print(variable_a)
  print(global_var)
  pass

## Enclosing Scope Example
### Enclosing scoped variable can be access/referenced from functions nested in another function where the variable resides. 
def outer():
  outer_var = "I am outer_var"
  def inner():
    print(outer_var)
  
  inner()
  print(outer_var)

if __name__ == "__main__":
  main()
  


