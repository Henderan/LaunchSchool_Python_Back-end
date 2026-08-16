from itertools import groupby

def crunch(text):
    return ''.join(key for key, group in groupby(text))

print(crunch('cccoonnnnttteent'))
