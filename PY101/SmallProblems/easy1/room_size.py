unit_lookup = {'m': 'meters', 'ft': 'feet'}

def prompt(message):
    return '==> ' + message

def unit_prompt():
    return prompt('Enter measurement unit: (m/ft): ')

def dimension_prompt(dim, unit):
    return prompt('Enter {dimension} of room (in {units}): '\
                  .format(dimension=dim, units=unit_lookup[unit]))

def display_area(area, unit):
    CONVERSION_FACTOR = 10.7639

    if unit == 'm':
        converted_area = area * CONVERSION_FACTOR
        converted_unit = 'ft'
    else:
        converted_area = area / CONVERSION_FACTOR
        converted_unit = 'm'

    print(f'\nArea of room: {area:.2f} square {unit_lookup[unit]} '
          f'({converted_area:.2f} square {unit_lookup[converted_unit]})')

def main():
    unit = ''
    while unit not in unit_lookup:
        unit = input(unit_prompt())

    length = float(input(dimension_prompt('length', unit)))
    width  = float(input(dimension_prompt('width', unit)))

    area = length * width
    display_area(area, unit)

main()
