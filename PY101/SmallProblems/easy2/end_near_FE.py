def middle(words):
    if len(words) == 0:
        return None    
    
    words_list = words.split()
    length = len(words_list)
    center = length // 2
    
    if length % 2 == 0:
        left_word = words_list[center - 1]
        right_word = words_list[center]
        return left_word + ' ' + right_word
    else:
        return words_list[center]

# These examples should print True
print(middle("my middle word") == "middle")
print(middle("Launch School is great!") == "School is")
print(middle("") == None)
print(middle("Python") == "Python")
