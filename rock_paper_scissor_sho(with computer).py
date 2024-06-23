import random

def play():
    user = input("Choose one -> 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer=random.choice(['r','s','p'])
    print(f"computer chose: {computer}")
    
    if user == computer:
        return 'It\'s a tie!'
    elif is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

print(play())
