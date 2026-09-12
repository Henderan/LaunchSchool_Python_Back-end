def stringy(size):
    result = ''
    for index in range(size):
        if index % 2 == 0:
            result += '1'
        else:
            result += '0'
            
    return result

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

