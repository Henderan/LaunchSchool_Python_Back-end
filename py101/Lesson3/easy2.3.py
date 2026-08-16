numbers = [42, 100, 101]
lower = 10
upper = 100



for number in numbers:
    print(f'Is {number} >= {lower} and <= {upper}? {number in range(lower, upper + 1)}') 
