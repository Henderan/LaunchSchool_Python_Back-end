def multiply(nums):
    product = 1
    for num in nums:
        product *= num
    return product

target_num = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')

numbers = range(1, target_num + 1)

if operation == 's':
    total = sum(numbers)
    print(f'\nThe sum of the integers between 1 and {target_num} is {total}.')
elif operation == 'p':
    product = multiply(numbers)
    print(f'\nThe product of the integers between 1 and {target_num} is {product}.')
else:
    print('\nTry again.')

