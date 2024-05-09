## **main() function**

### **1. : Functions**
```python
def say_hello(name):
  print("Hello " + name + "!")

def say_goodbye():
  print("Goodbye!")
```
- These are some of the functions in the program that will be called in main().

### **2. : main()**
```python
def main():
  say_hello("Shawn")
  print("Welcome to The Young Maker")
  say_goodbye()

if __name__ == "__main__":
  main()
```
- Using `main()`, we can control the order of the functions being called and executed.
