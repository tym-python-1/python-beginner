# Instructions
1. Debug the code `main.py`.
2. `function_a()` should ask user for 2 input and returns the sum of the inputs.
3. The code works correctly. However, `num1` and `num2` are currently global variables; they should only exist when `function_a()` is being executed.
4. Once you are done, raise your hand for your teacher to check! :)

## Example Input and Output

### Example 1
#### Example Input
```plaintext
1
2
```
#### Example Returned Value #1
```plaintext
3
```
_**Explanation:** The `function_a` function adds `1` and `2` and returns `3`._

## Hint
1. For a variable to exist only when a function is running, it must have a local scope in the function.

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
- Before submitting, ensure that your function is using local variables and correctly sums the number.
   ![image](submit.png)
