from datetime import datetime

current_year = datetime.today().year

current_age    = int(input('What is your age? '))
retirement_age = int(input('At what age would you like to retire? '))

years_remaining = retirement_age - current_age
retirement_year = current_year + years_remaining 

print(f"\nIt's {current_year}. You will retire in {retirement_year}.")
print(f"You have only {years_remaining} years of work to go!")

