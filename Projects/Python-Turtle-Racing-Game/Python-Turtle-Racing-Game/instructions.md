# Instructions
![image](image.png)
1. In your `main.py` file, begin by importing the `turtle`, `random`, and `time` modules.
2. Define a function `function_a` which simply returns the value `1`.
3. Set up constants for the racing game, such as `TRACK_X`, `TRACK_Y`, `TRACK_LEN`, `TRACK_WIDTH`, and others that define the racing track's appearance.
4. Write a `setup_screen` function that initializes the turtle screen with appropriate dimensions, title, background color, and other necessary settings.
5. Create a `draw_track` function to draw the race track and lanes on the turtle screen.
6. Define a `draw_finishline` function that draws the finish line for the race with alternating white and black squares.
7. Write a `setup_turtles` function to create and set up four racing turtle objects with distinct colors, sizes, and starting positions.
8. Use the `get_userguess` function to prompt the user to guess which turtle will win the race. The input should be a number between 1 and 4.
9. Implement the `race` function which simulates the turtles racing towards the finish line. The function should move each turtle a random number of steps at a time until one crosses the finish line.
10. Display the winner of the race and compare it with the user's guess to inform them whether they've guessed correctly.
11. Finally, wrap the setup and execution of the game in a `main` function and execute the `main` function when the script is run.

## Example
### Example Setup
- Start the program, and a graphical window will open, displaying the turtle race track.
- The program will prompt you to guess which turtle will win.
  
### Example Output
- Watch as the turtles race towards the finish line.
- After the race ends, the program will display whether your guess was correct or not.

## Hint
1. The `turtle` module provides a graphical window and turtle objects that can be moved and manipulated to create drawings.
2. The `random.randint(a, b)` function from the `random` module can be used to get a random integer between `a` and `b`.
3. The `time.sleep(seconds)` function from the `time` module can be used to introduce a delay in the execution.


## Final Note
- This turtle race game is a fun graphical way to learn and practice Python programming. Experiment with different track designs, turtle speeds, or race mechanics to make the game even more exciting!
