lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def divisible_by_3(lst):
    return [num for num in lst if num % 3 == 0]

new_list = [divisible_by_3(sublist) for sublist in lst]

print(new_list)
