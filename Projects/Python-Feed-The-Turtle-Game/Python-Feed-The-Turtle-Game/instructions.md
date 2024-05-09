# Instructions
![image](image_4.png)
1. In your `main.py` file, begin by importing the `turtle`, `random`, and `time` modules.
2. Setup the turtle screen by creating a screen variable using the `turtle.Screen()` function.
3. Create a turtle object for the player to control using the `turtle.Turtle()` function.
4. Create a food target object `turtle.Turtle()`.
5. Create a score display.
6. Create a timer display.
7. Define 4 movement function `move_up()`, `move_down()`, `move_left()` and `move_right()`.
8. Bind the 4 movement function to the arrow keys using `screen.onkey(function, key)` function.
9. Define a `check_collision()` function to check when the turtle touch the target.
10. Define a `move_target()` function to randomly move target.
11. Define a `countdown(time_left)` function to specify game duration and update countdown timer.
12. Define an `end_game()` function to end game and display game over.
13. Bind the `Escape` key to call the `end_game()` function.
14. Call the `countdown(time_left)` function and specify game duration.
15. Create main game loop using the concept of infinite loop.

## Example
### Example Setup
- Start the program, and a graphical window will open, displaying the game screen.
- Player can control the turtle with the arrow keys.
  
### Example Output
- Eat as many targets as you can within 60 seconds.
- After 60 seconds or if `esc` key is pressed, the game will end and display the score.

## Hint
1. The `turtle` module provides a graphical window and turtle objects that can be moved and manipulated to create drawings.
2. Enable listener for specific screen using `screen.listen()`
3. Create keybinds using `screen.onkey(function, key)` 
4. 


## Final Note
- This Feed the Turtle Game is a fun graphical way to learn and practice Python programming. Experiment with different mechanics to make the game even more exciting!
