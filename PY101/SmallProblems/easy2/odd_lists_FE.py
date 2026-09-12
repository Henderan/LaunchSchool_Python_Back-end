def oddities(a_list):
    return [val for idx, val in enumerate(a_list) if idx % 2 == 1]

print(oddities([2, 3, 4, 5, 6]) == [3, 5])  # True
print(oddities([1, 2, 3, 4]) == [2, 4])        # True
print(oddities(["abc", "def"]) == ['def'])     # True
print(oddities([123]) == [])                # True
print(oddities([]) == [])                      # True

