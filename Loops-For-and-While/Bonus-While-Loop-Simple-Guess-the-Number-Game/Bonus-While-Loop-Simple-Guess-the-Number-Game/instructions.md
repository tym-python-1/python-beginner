# Instructions
1. Write a program in `main.py` that reads a sequence of integers, each written in a separate line.
2. The program stops asking the user for input once the user guesses the correct number.
3. The program should print if the user is correct, too low or too high.
4. You may use the provided variable `target_number` that will give you a random integer between 1 to 10 using python's random library (We will learn more about library in the future)

## Example Input and Output

### Example 1
#### Example Input #1
```plaintext
1
4
2
3
```
#### Example Output #1
```plaintext
Too low
Too high
Too low
Correct! The number is 3.
```
_**Explanation:** Each number the user inputs, the program replies with a message. The user inputs `1` which is too low, so the user guesses a higher number until he guesses `3` which is the correct number and the program congratulates the user and ends._

### Example 2
#### Example Input #2
```plaintext
5
6
7
```
#### Example Output #2
```plaintext
Too low
Too low
Correct! The number is 7.
```

## Hint
1. Keep taking the input in a loop until the correct number is guessed.
2. Compare the user input with the correct number and print if the number is too high or too low.
3. When correct number is guessed, congratulate the user and end the game.

## Test Your Code
### Running Tests
- To verify your game is working, ask your teacher to try your game!

## Final Note
- Ensure your program correctly tell the user if the input is too low/high indefinetly until the user finally guesses correctly.
   ![image](submit.png)
