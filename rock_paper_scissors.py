import random

computer_choice = "paper"

def get_choices():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def player_input():
    user_input = input("Please enter your choice (rock, paper, or scissors):")
    return user_input

def play_game():
    choices = get_choices()
    if choices["player"] == "rock" and choices["computer"] == "rock":
        return "tie"
    elif choices["player"] == "rock" and choices["computer"] == "paper":
        return "computer wins"
    elif choices["player"] == "rock" and choices["computer"] == "scissors":
        return "player wins"
    elif choices["player"] == "paper" and choices["computer"] == "paper":
        return "tie"
    elif choices["player"] == "paper" and choices["computer"] == "rock":
        return "player wins"
    elif choices["player"] == "paper" and choices["computer"] == "scissors":
        return "computer wins"
    elif choices["player"] == "scissors" and choices["computer"] == "scissors":
        return "tie"
    elif choices["player"] == "scissors" and choices["computer"] == "rock":
        return "computer wins"
    elif choices["player"] == "scissors" and choices["computer"] == "paper":
        return "player wins"



player_choice = player_input()

print(get_choices())

print(play_game())