def print_in_box(message, max_length=None):
    if max_length and len(message) > max_length:
        message = message[:max_length + 1]
        
    horizontal_rule = f'+-{'-' * len(message)}-+'
    empty_line = f'| {' ' * len(message)} |'
    
    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)
    
print_in_box('To boldly go where no one has gone before.')
print_in_box('')
print_in_box('This sentence is longer than will fit in the specified maximum length', 60)
