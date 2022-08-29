import random

top_range = input('Type a top range for your guess: ')
if top_range.isdigit:
    top_range=int(top_range)

    if top_range<0:
        print('Please guess number above zero')
        quit()
else:
    print('Please type a number')
    quit()

random_number = random.randint(0, top_range)

guesses=0
while True:
    guesses +=1
    User_guess = input('Type your guess: ')
    if User_guess.isdigit:
        User_guess=int(User_guess)
    else:
        print('Please type a number')
        continue
    
    if User_guess==random_number:
        print('Your guess is correct, you got it!')
        break
    elif User_guess<random_number:
        print('Your guess below number')
    else:
        print('Your guess above number')

print('You got it in',guesses,'guesses')