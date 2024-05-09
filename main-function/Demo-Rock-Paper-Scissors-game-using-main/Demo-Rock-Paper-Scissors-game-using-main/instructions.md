## **main() function**

### **1. : Game Functions**
```python
def welcome():
  name = input("Enter username: ")
  print("Hello " + name + "!")
  print("Welcome to a game of rock, paper, scissors")
  
def player_turn():

  player_action = input("Enter a choice (rock, paper, scissors): ")
  if(player_action != "rock" and player_action != "paper" and player_action != "scissors" ):
    print("\nInvalid option please try again!")
    return player_turn()
  else:
    return player_action

def computer_turn():
  actions = ["rock", "paper", "scissors"]
  action = random.choice(actions)
  print("\nComputer chose " + action)
  return action

def announce_winner(player_action, computer_action):
  print()
  if player_action == computer_action:
    print("It was a tie!")
  elif player_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
  elif player_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
  elif player_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
```
- Using multiple functions, we can organise code and make it easier for us to understand.
- **welcome()**: Ask for username and welcomes the player.
- **player_turn()**: Ask player for their action.
- **computer_turn()**: The computer randomly chooses an action.
- **annouce_winner()**: Determines and announces the winner after the player and computer have their turn.

### **2. : main()**
```python
def main():
  welcome()
  player_action = player_turn()
  computer_action = computer_turn()
  announce_winner(player_action, computer_action)

if __name__ == "__main__":
  main()
```
- Using `main()`, we can control the order of the functions being called. The naming of functions is crucial and makes it easy for us to understand the flow of the game without having to read all the code.
