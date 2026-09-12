lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

my_dict = {key: value for [key, value] in lst}

print(my_dict)
