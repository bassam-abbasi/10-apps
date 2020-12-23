import random

print('----------------------------------')
print('   GUESS WHAT IS THE NUMBER ')
print('----------------------------------')
print()

the_number = random.randint(0, 100)
name = input("Player, what is your name? ")
guess = -1
while True:
    guess_text = input('{0}, Guess the number between 0 and 100: '.format(name))
    guess = int(guess_text)

    if guess < the_number:
        print("{0}, Your guess of {1} is too low".format(name, guess))
    elif guess > the_number:
        print("{0}, Your guess of {1} is too high".format(name, guess))
    else:
        print("Hey {}, You WIN!".format(name))
        exit()

