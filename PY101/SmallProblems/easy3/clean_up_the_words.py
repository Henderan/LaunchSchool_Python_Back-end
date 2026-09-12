def clean_up(text):
    clean_text = ''
    
    for char in text:
        if char.isalpha():
            clean_text += char
        elif clean_text == '' or clean_text[-1] != ' ':
            clean_text += ' '
            
    return clean_text

print(clean_up("---what's my +*& line?") == " what s my line ")
