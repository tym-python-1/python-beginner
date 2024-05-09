# Instructions
1. Write a program in `main.py` that prompts the user to input 1 integers representing the height of the triangle.
2. The program should then output a left-aligned triangle made of asterisks (*), with the height corresponding to the inputted number.

## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
5
```
#### Example Output #1
```plaintext
*
**
***
****
*****
```

_**Explanation:** The user inputs `5` for height. The program then prints a left-aligned triangle made of asterisks with 5 rows, each row down the width/column increases by 1._

### Example 2
#### Example Input #2
```plaintext
3
```
#### Example Output #2
```plaintext
*
**
***
```

_**Explanation:** The user inputs `3` for height. The program then prints a left-aligned triangle made of asterisks with 3 rows, each row down the width/column increases by 1._

## Hint
1. Use the `input()` function to take an integer input from the user for the number of rows.
2. Convert the input to an integer before performing the operation.
3. Use a loop to print the desired triangle. The loop variable should control the number of asterisks printed in each row.
4. Note the pattern, 1st row will print 1 star, 2nd row will print 2 start, 3rd row will print 3 star.

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
- Before submitting, ensure that your program correctly prints a left-aligned triangle with the height specified by the user.
   ![image](submit.png)
