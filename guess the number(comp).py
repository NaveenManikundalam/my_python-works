import random


def play():
    user = input("'r' for Rock, 'p' for Paper,'s' for Scissors: ")
    comp = random.choice(['r','p','s'])

    if user == comp:
        print('You chose:',user)
        print('The computer chose:',comp)
        return 'It\'s a tie'

    if win(user,comp):
        print('You chose:',user)
        print('The computer chose:',comp)
        return 'Hey, you Won!!!'
    else:
        print('You chose:',user)
        print('The computer chose:',comp)
        return 'You Lost. Computer won'
    
def win(player,opponent):
    if (player == 'r' and opponent == 's')\
        or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True


print(play()) 
