import random

print('Welcome to the higher/lower game, Bella')
lower_bound = int(input('Enter the lower bound: '))
upper_bound = int(input('Enter the upper bound: '))

random_number = random.randint(lower_bound, upper_bound)

guess = int(input(f'Great, now guess a number between {lower_bound} and {upper_bound}: '))

while guess != random_number:
    if guess < lower_bound or guess > upper_bound:
        print(f'Make sure the number is between {lower_bound} and {upper_bound}!')
        guess = int(input('Guess another number: '))
    elif guess < random_number:
        print('Nope, too low')
        guess = int(input('Guess another number:'))
    elif guess > random_number:
        print('Nope, too high')
        guess = int(input('Guess another number: '))

print('You got it!')


