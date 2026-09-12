munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for name, info in munsters.items():
    print(f"{name} is a {info['age']}-year-old {info['gender']}.")

# or
# for munster in munsters:
#    print(f"{munster} is a {munsters[munster]['age']}-year-old {munsters[munster]['gender']}.")
