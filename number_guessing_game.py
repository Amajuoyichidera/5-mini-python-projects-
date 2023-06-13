# import random

# number_range = input('Enter a number: ')

# if number_range.isdigit():
#     number_range = int(number_range)

#     if number_range <= 0:
#         print('Please enter number bigger than zero')
#         quit()
# else : 
#     print('please enter a number')
#     quit()

# random_number = random.randint(0, number_range)
# print(random_number)

# guessed = 0

# while True:
#     guessed += 1
#     user_guess = input('Make a guess: ')
#     if user_guess.isdigit():
#         user_guess = int(user_guess)   
#     else : 
#         print('please enter a number: ')
#         continue


#     if user_guess == random_number:
#         print('Correct!!')
#         break
#     elif user_guess > random_number:
#         print('You went above the number')
#     else:
#         print('You went below the number')

# print(f'you got it in {guessed} guesses')




import random
number_range = input('Enter number: ')

if number_range.isdigit():
    number_range = int(number_range)

    if number_range <= 0:
        print('Enter number bigger than 0')
        quit()

else:
    print('enter a number ')
    quit()

random_number = random.randint(0, number_range)
print(random_number)

while True:
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('enter a number ')
        continue

    if user_guess == random_number:
        print('Correct')
        break
    else :
         print('wrong')

        
