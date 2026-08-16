def prompt(message):
    print(f'\n==> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number < 0:
            raise ValueError(f'Value must be > 0" {number_str}')
    except ValueError:
        return True

    return False

prompt('Welcome to Loan Calculator!')

proceed = 'y'

while proceed == 'y':
    
    prompt('Enter loan amount: ')
    loan_amount_str = input()
    while invalid_number(loan_amount_str):
        prompt('Must enter a loan amount >= 0')
        loan_amount_str = input()

    prompt('Enter annual interest rate (e.g. for 5% enter 5): ')
    annual_rate_str = input()
    while invalid_number(annual_rate_str):
        prompt('Must enter an annual interest rate >= 0')
        annual_rate_str = input()
    
    prompt('Enter loan term in years: ')
    term_in_years_str = input()
    while invalid_number(term_in_years_str):
        prompt('Must enter a loan term >= 0')
        term_in_years_str = input()

    loan_amount = float(loan_amount_str)
    annual_rate = float(annual_rate_str) / 100
    monthly_rate = annual_rate / 12
    term_in_years = float(term_in_years_str)
    term_in_months = term_in_years * 12

    monthly_payment = loan_amount * (monthly_rate / 
                  (1 - (1 + monthly_rate)**(-term_in_months)))

    prompt(f'The monthly payment is: ${monthly_payment:,.2f}\n')

    while True:
        prompt('Do you wish to perform another calculation? (y/n): ')
        proceed = input().lower()

        if proceed in ['y', 'n']:
            break
