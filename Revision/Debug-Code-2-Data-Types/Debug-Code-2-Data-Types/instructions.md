# Instructions
1. Write a program in `main.py` that ask the user for 4 values; name, age, weight and height. The values should have the data type of String, Integer, Float and Float respectively.
2. The program should then concatenate the text and input together and print the user's details.
3. The formula for bmi is given in the code

## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
Please enter your name: John
Please enter your age: 18
Enter your weight(kg): 51.50
Enter your height(m): 1.65
```

#### Example Output #1
```plaintext
My name is John and I am 18 years old.
My bmi is 18.916437098255283.
In 5 years, I will be 23 years old.
```

_**Explanation:** The program concatenates the the input, calculates bmi and age in 5 years then prints the result._

## Hint
1. Remember typecasting functions such as `str()`, `int()` and `float()`
2. One way to concatenate string is to use the `+` operator.
3. Another way is to use string format. E.g. `"My name is {}, I'm {}".format("John",36)`

## Test Your Code
### Running Tests
- To verify your program, run it and check if it provides the correct output based on the given inputs.
   ![image](tests_tools.png)
- If the output is correct, and there are no errors, proceed to submit it.
   ![image](submit.png)

### Test Results
- If your code passes all the tests, you will see the following screen.
   ![image](pass.png)
- If any test case fails, analyze the `Results` section to identify the error and refine your code.
   ![image](fail_tests.png)
   ![image](results.png)

## Final Note
- Before submitting, ensure that your program is able to execute and prints expected output.
   ![image](submit.png)
