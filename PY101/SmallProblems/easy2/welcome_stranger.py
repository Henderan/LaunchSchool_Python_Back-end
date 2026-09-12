def greetings(names, job_info):
    return (f'Hello, {' '.join(names)}! Nice to have a '
            f'{job_info['title']} {job_info['occupation']} around.') 

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

