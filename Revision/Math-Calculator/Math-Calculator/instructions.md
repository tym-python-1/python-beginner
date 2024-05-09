# Instructions
1. Write a program in `main.py` that takes 3 inputs from the user to perform basic mathematical operation.
2. The first input is a string that tells the program which math operation to perform; add, minus, times or divide.
3. The second and third input are 2 integers to perform the math operation.
4. Finally, the program should print the results of the calculation.

## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
Math operation(add/minus/times/divide): add
First number: 1
Second number: 2
```
#### Example Output #1
```plaintext
3
```
_**Explanation:** The program adds 1 and 2 and prints 3 as the result._

### Example 2
#### Example Input #2
```plaintext
Math operation(add/minus/times/divide): divide
First number: 1
Second number: 2
```
#### Example Output #2
```plaintext
0.5
```
_**Explanation:** The program divides 1 and 2 and prints 0.5 as the result._

## Hint
1. Use the `input()` function thrice to take a string and two integer inputs from the user.
2. Convert the inputs to integers before performing the calculation.
3. Use a conditional statement (`if`, `elif`, `else`) to identify the math operation to perform.

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
- Before submitting, ensure that your program correctly performs the math operation and prints the calculated result.
   ![image](submit.png)
