import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('You chose:',user)
        print('Computer chose:',computer)
        return 'It\'s a tie'

    if is_win(user, computer):
        print('You chose:',user)
        print('Computer chose:',computer)
        return 'You won!'

    else:
        print('You chose:',user)
        print('Computer chose:',computer)
        return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') \
       or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
