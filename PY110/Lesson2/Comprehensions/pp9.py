lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def has_only_evens(dct):
    lists = list(dct.values())
    flattened_elements = [num for lst in lists for num in lst]
    evens = [num for lst in lists for num in lst if num % 2 == 0]
    return len(flattened_elements) == len(evens)

evens = [item for item in lst if has_only_evens(item)]

# alternative:
# evens = [item for item in lst if all(num % 2 == 0 for lst in list(item.values()) for num in lst)]

print(evens)
