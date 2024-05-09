# Instructions
1. Write a program in `main.py` that first takes a single integer `N` as input, which represents the number of integers to follow.
2. Then, take `N` integers as input, each separated by a new line.
3. Calculate the average of these `N` integers and print it.

## Constraints
- The first line of input will contain the integer `N` (1 ≤ `N` ≤ 100).
- Each of the next `N` lines will contain one integer, representing the numbers whose sum needs to be calculated then averaged.

## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
10
1
2
1
1
1
1
3
1
1
1
```
#### Example Output #1
```plaintext
1.3
```

## Hint
1. First, take the integer `N` as input, representing the number of integers to follow.
2. Use a for loop and the `range(N)` function to take `N` integers as input.
3. In each iteration of the loop, convert the input to an integer and add it to the running total.
4. After the loop, calculate the average of all the values.
5. Print the average calculated.

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
- Before submitting, ensure that your program correctly calculates the average of the `N` input numbers and handles varying values of `N`.
   ![image](submit.png)
