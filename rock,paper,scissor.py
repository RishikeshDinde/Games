import random

user_win = 0
computer_win = 0


while True:

    options = ['rock','paper','scissors']
    user_input = input('if you want to play, type Rock/Paper/Scissors or Q to Quite: ').lower()
    if user_input=='q':
        break
    if user_input not in options:
        continue

    random_input = random.randint(0,2) 
    
    computer_pick = options[random_input]
    print(computer_pick)
    print("Computer pick:",computer_pick)

    if user_input=='rock' and computer_pick =='scissors' :
        print('You win!')
        user_win+=1
    elif user_input=='paper' and computer_pick =='rock' :
        print('You win!')
        user_win+=1
    elif user_input=='scissors' and computer_pick =='paper' :
        print('You win!')
        user_win+=1
    else :
        print('You lost!')
        computer_win +=1

    
    print("You win",user_win,'times.')
    print("Computer win",computer_win,'times.')
