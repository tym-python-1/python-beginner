# Instructions
1. Write a program in `main.py` that takes in a string from the user.
2. Then, check if the string is a palindrome.
3. Prints True/False to indicate if string is a palindrome.

Palindrome refers to a word that reads the same forward and backwards. For instance, radar and kayak are read the same forward and backwards!


## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
madam
```
#### Example Output #1
```plaintext
True
```
### Example 2
#### Example Input #2
```plaintext
apple
```
#### Example Output #2
```plaintext
False
```
### Example 3
#### Example Input #3
```plaintext
hannah
```
#### Example Output #3
```plaintext
True
```

## Hint
1. First, check using `String[start]` if the left most character matches the right most.
2. If it does not match, we immediately know it is not a palindrome.
3. Check the next left inner character and the next right inner character.
4. Rinse and repeat until we reach the final letter towards the center.
5. Print True/False if the string is a palindrome.

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
- Before submitting, ensure that your program correctly tell us is the input string is a palindrome.
   ![image](submit.png)
