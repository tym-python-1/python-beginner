# Instructions
1. Write a program in `main.py` that reads a sequence of non-negative integers, each written in a separate line.
2. The sequence ends when `0` is encountered, and `0` is not considered part of the sequence.
3. The program should print the number of elements in the sequence that are greater than their previous number.

## Constraints
- The input sequence will contain at least one number, and the sequence is terminated by `0`.
- All numbers in the sequence are non-negative integers.

## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
1
2
3
4
5
0
```
#### Example Output #1
```plaintext
4
```

### Example 2
#### Example Input #2
```plaintext
1
2
3
0
5
6
```
#### Example Output #2
```plaintext
2
```
_**Explanation:** The sequence ends at the 4th line. Line 2 number is greater than Line 1 number, and Line 3 number is greater than Line 2 number. The count of numbers that are greater than the previous number in the sequence is thus `2`._

## Hint
1. Keep taking the input in a loop until `0` is encountered.
2. Compare the current number with the previous number in each iteration and increase the count if the current number is greater.
3. When `0` is encountered, break out of the loop and print the count of numbers that are greater than their previous number.

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
