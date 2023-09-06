# We will write a rock paper scissors game in class - Complete it in this file

# We have player and computer
    # Computer chooses a random number for rock, paper, or scissors
import random

player_choice = "rock"
computer_choice = "paper"

def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = "rock"
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

choices = get_choices()

print(choices)
# Player input uses rock paper or scissors

# Store in a dictionary

# Run a function to see who wins