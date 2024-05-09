## **Python Programming Concepts**

### **1. Importing Modules and Libraries:**
```python
import math
import random
import requests
from constants import cat_image, dog_image, greetings
```
- **Import Keyword:** Used to import modules into a file.
- **Import Statements:** Always located at the top of the file.

### **2. Math Module:**
```python
print(math.pi)  # Gets the value of pi from the math module

print(math.factorial(4))  # Gets the factorial of 4
print(math.ceil(4.3))  # Rounds the number UP to the nearest whole number
print(math.floor(4.3))  # Rounds the number DOWN to the nearest whole number
print(math.pow(2, 3))  # 2 raised to the power of 3
```
- **Math Module:** Provides a range of constants and functions related to mathematical operations.

### **3. Random Module:**
```python
print(random.randrange(10))  # Generates a random number between 0 to 10
```
- **Random Module:** Provides functions to generate random numbers.

### **4. Using Imported Functions and Constants:**
```python
print(cat_image)
print(dog_image)
greetings("John")
```
- **Importing From Files:** We can import constants and functions created in other files.

### **Note:**
- **`requests` Module:** Allows sending HTTP requests using Python. This topic is out of scope for this lesson.
- **Organization:** Keeping code well-organized is crucial. It includes appropriately placing import statements and keeping related pieces of code together.

### **Out of Scope:**
The `requests` module is briefly mentioned, but exploring it is out of the scope for this lesson. It allows you to send HTTP requests using Python and is crucial in interacting with the web and web-based services.
