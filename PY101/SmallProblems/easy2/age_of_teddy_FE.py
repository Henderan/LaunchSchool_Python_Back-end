from random import randint

def display_result(name, age):
    print(f'{name} is {age} years old!')

name = input('==> What is your name? ')
if name == '':
    name = 'Teddy'
age = randint(20, 100)

display_result(name, age)
