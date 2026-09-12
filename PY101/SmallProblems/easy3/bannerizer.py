def print_in_box(message):
    horizontal_rule = f'+-{'-' * len(message)}-+'
    empty_line = f'| {' ' * len(message)} |'
    
    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)
    
print_in_box('To boldly go where no one has gone before.')
print_in_box('')
