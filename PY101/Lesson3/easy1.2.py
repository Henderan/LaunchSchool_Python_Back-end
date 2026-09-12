str1 = "Come over here!"
str2 = "What's up, Doc?"
strings = [str1, str2]

for s in strings: 
    print(f'Does "{s}" end with "!"? {s.endswith('!')}')
