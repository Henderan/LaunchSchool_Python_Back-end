lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_list = [{key: value + 1} for subdict in lst for key, value in subdict.items()]

print(new_list)
