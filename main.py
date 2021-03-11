# Exercise 1 and 2 in one file


import math
import random
name = input('Enter username:')
age = input('Age:')
nextTenth = int(math.ceil(int(age)/10.0)) *10
timeleft = nextTenth - int(age)
print('Hello ' + name + ', you have ' + str(timeleft) + ' years left, until you are ' + str(nextTenth) + ' years old')


random = random.randrange(101)
print(random)

found: bool=False
while not found:
    guess= int(input('Guess a number between 0 and 100: '))
    if guess==random:
        print('That\'s the right number')
        found=True

    if random>guess:
        print('The number is higher')

    if random<guess:
        print('The number is lower')
