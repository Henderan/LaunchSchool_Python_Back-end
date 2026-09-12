lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_list = [sorted(sublist, key=str) for sublist in lst]

print(new_list)
