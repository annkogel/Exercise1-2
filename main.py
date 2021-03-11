import math
name = input('Enter username:')
age = input('Age:')
nextTenth = int(math.ceil(int(age)/10.0)) *10
timeleft = nextTenth - int(age)
print ('Hello ' + name + ', you have ' + str(timeleft) + ' years left, until you are ' + str(nextTenth) + ' years old')

