# Instructions
1. Write a program in `main.py` that takes two inputs from the user: `height` (in meters) and `weight` (in kilograms).
2. The program should then calculate the Body Mass Index (BMI) using the formula:
   ![2](2.2.%20bmi%20img%201.png)
   - Note: Both inputs need to be converted to `float` type before performing the calculation.
3. Finally, the program should print the BMI as a whole number. Use the `round()` function to round the result to the nearest whole number.

## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
1.8
65
```
#### Example Output #1
```plaintext
20
```
_**Explanation:** The program takes 1.8 as height and 65 as weight, calculates the BMI and prints it as a whole number._

## Hint
1. Use the `input()` function twice to take user inputs for height and weight.
2. Convert both inputs to float before performing calculations.
3. Use the exponent operator `**` to square the height.
4. Apply PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction) rule for calculations.
5. Use the `round()` function to round off the BMI value to the nearest whole number.

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
- Before submitting, ensure that your program correctly calculates and prints the BMI for any given height and weight.
   ![image](submit.png)
