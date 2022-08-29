name =input('Give your name: ')
print('Welcome to my computer quize! '+name)
playing = input('Do you want to play game: ')

if playing.lower() != 'yes':
    quit()
else:
    print('Okay lets play! '+name)

score = 0


answer = input('What is the full form of CPU?  ')
if answer.lower() =='computer processing unit':
    print('you are correct')
    score+=1
else:
    print('Incorrect')

answer = input('which language we using now?  ')    
if answer.lower() =='python':
    print('you are correct')
    score+=1
else:
    print('Incorrect')

answer = input('The first mechanical computer designed by Charles Babbage was called ?  ')
if answer.lower() =='analytical engine':
    print('you are correct')
    score+=1
else:
    print('Incorrect')

answer = input(' Which is a single integrated circuit?  ')
if answer.lower() =='gate':
    print('you are correct')
    score+=1
else:
    print('Incorrect')

answer = input('A desktop computer is also known as  ')
if answer.lower() =='pc':
    print('you are correct')
    score+=1   
else:
    print('Incorrect')


print('Congratulations you got ' +str(score)+' marks')
print('Congratulations you got'+str((score/5)*100)+'%')
