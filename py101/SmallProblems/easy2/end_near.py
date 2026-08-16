def penultimate(words):
    return words.split()[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

