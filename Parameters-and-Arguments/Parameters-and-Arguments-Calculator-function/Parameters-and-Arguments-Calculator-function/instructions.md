# Instructions
1. Write a function named `calculator` in `main.py` that have 3 parameter.
2. First parameter is to specify the math operation to perform. The possible values includes `add`, `minus`, `times` and `divide`.
3. The second and third parameter are the 2 **integers** to perform the math operation on.
4. The function should return the result of the calculation.

## Example Input and Output

### Example 1
#### Example Argument #1
```plaintext
calculator("minus", 6, 5)
```
#### Example Returned Value #1
```plaintext
1
```
_**Explanation:** The `calculator` function takes in 3 arguments `"minus"`, `6` and `5`. It then calculates `6-5`, and returns the result `1`._

### Example 2
#### Example Argument #2
```plaintext
calculator("divide", 10, 5)
```
#### Example Returned Value #2
```plaintext
2.0
```
_**Explanation:** The `calculator` function takes in 3 arguments `"divide"`, `10` and `5`. It then calculates `10/5`, and returns the result `2.0`._

## Hint
1. The function requires 3 parameter seperated by a comma the order of the parameter is important.
2. Using `if`,`elif` statements check which math operation to perform.
3. `Return` the result of the math operation performed on the 2 values.

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
- Before submitting, ensure that your function correctly performs the math operation and returns the result.
   ![image](submit.png)
