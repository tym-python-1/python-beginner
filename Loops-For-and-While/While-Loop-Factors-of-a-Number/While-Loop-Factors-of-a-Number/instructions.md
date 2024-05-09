# Instructions
1. Write a program in `main.py` that takes in one positive integer.
2. Using a while loop the program will find and print all the factors of the positive integer from the smallest to largest factor.

## Constraints
- The input sequence will be a positive value.

## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
8
```
#### Example Output #1
```plaintext
1
2
4
8
```
_**Explanation:** The user inputs `8`, now we print all the factors including `1` and `8` itself since they are also factors._

### Example 2
#### Example Input #2
```plaintext
12
```
#### Example Output #2
```plaintext
1
2
3
4
6
12
```

## Hint
1. Obtain an integer input from the user.
2. Using a while loop, we know if a number is a factor if the input is divisible by that number. Recall the `%` operator.
3. Print all of the factors.

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
- Ensure your program correctly counts the numbers in varying sequences that are greater than their previous number and respects the `0` terminator before submitting your fully verified implementation.
   ![image](submit.png)
