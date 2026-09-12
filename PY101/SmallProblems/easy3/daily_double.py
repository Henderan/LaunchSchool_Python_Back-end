def crunch(string):
    crunched_string = ''
    prior_char = ''
    
    for char in string:
        if char != prior_char:
            crunched_string += char
            prior_char = char
            
    return crunched_string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

