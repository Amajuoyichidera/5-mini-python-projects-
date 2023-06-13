print('Welcome to my computer game')

playing = input('Do you want to play my game ?  ')

if playing.lower() != 'yes' :
    quit()
print("Okay let's roll ")

score = 0

answer = input('what is the Full meaning of C.P.U? ')
if answer.lower() == 'central processing unit':
    print('Correct')
    score += 1
else : 
    print('incorrect')


answer = input('what is the Full meaning of G.P.U? ')
if answer.lower() == 'graphic processing unit':
    print('Correct')
    score += 1
else : 
    print('incorrect')


answer = input('what is the Full meaning of R.A.M? ')
if answer.lower() == 'random access memory':
    print('Correct')
    score += 1
else : 
    print('incorrect')


# print('you got' + str(score) + 'questions correct' )
# or
print(f'you got {score} questions correct')
print(f'you got {score / 3 * 100 } %')