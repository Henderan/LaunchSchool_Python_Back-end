dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def transform_item(dct):
    if dct['type'] == 'fruit':
        colors = [color.capitalize() for color in dct['colors']]
        return colors
    else:
        size = dct['size'].upper()
        return size

lst = [transform_item(item) for item in dict1.values()]

print(lst)
