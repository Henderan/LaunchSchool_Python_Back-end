lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_of_odds(lst):
    odds = [num for num in lst if num % 2 == 1]
    return sum(odds)

new_list = sorted(lst, key=sum_of_odds)

print(new_list)
