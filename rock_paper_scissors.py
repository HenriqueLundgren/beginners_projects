import random

def play():
    # read the user's choice
    user = input("What's your choice?? 'r' for rock, 'p' for paper or 's' for scissors\n").lower()
    # computer randomize the objects
    computer = random.choice(['r', 'p', 's']).lower()

    if user == computer:
        return "It's a tie"

    # get the fuction victory, basic is replacing the conditions that has a win
    if victory(user, computer):
        return "You won!!"

    # we don't need the if statement here, because we only can reach this line if the others were not \
    # satisfied
    return "You lost!!"

def victory(player, opponent):

    # the player won if this conditions are correct: r > s, p > r, s > p
    if (player == 'r' and opponent == 'p') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True

print(play())