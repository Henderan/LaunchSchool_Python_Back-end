def multiply(num1, num2):
    return num1 * num2

def power(base, exponent):
    result = 1
    for number in range(exponent):
        result = multiply(result, base)
    return result

print(power(5, 3) == 125)   # True
print(power(-8, 2) == 64)  # True
