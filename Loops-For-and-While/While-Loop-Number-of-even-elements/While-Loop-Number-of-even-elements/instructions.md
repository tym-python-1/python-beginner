# Instructions
1. Write a program in `main.py` that reads a sequence of non-negative integers, each written in a separate line.
2. The sequence ends when `0` is encountered, and `0` is not considered part of the sequence.
3. The program should print the number of even elements in the sequence.

## Constraints
- The input sequence will contain at least one number, and the sequence is terminated by `0`.
- All numbers in the sequence are non-negative integers.
  
## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
2
1
4
0
```
#### Example Output #1
```plaintext
2
```

### Example 2
#### Example Input #2
```plaintext
2
0
4
2
4
```
#### Example Output #2
```plaintext
1
```
_**Explanation:** The sequence ends with `0`, even when there are more inputs; we do not consider them as the sequence would have ended at the 2nd input and there is only one even number in the sequence, which is `2`._

## Hint
1. Keep taking the input in a loop until `0` is encountered.
2. In each iteration, check if the number is even and increase the count of even numbers accordingly.
3. When `0` is encountered, break out of the loop and print the count of even numbers.

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
- Ensure your program correctly counts the even numbers in varying sequences and respects the `0` terminator before submitting your fully verified implementation.
   ![image](submit.png)
