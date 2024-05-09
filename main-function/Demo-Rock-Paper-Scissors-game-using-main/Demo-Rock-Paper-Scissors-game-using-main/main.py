import random

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

  
def main():
  welcome()
  player_action = player_turn()
  computer_action = computer_turn()
  announce_winner(player_action, computer_action)

if __name__ == "__main__":
  main()
  


