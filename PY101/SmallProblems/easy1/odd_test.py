def is_odd(number):
    return abs(number) % 2 == 1
    
numbers = [-3, -4, 5, 6]

for number in numbers:
    print(f'is {number:>2} odd? {is_odd(number)}')
