def prompt(message):
    return '==> ' + message
    
def calculate(num1, num2, operator):
    match operator:
        case '+':  return num1 + num2
        case '-':  return num1 - num2
        case '*':  return num1 * num2
        case '/':  return num1 / num2
        case '//': return num1 // num2
        case '%':  return num1 % num2
        case '**': return num1 ** num2

float1 = float(input(prompt('Enter the first number:\n')))
float2 = float(input(prompt('Enter the second number:\n')))
    
for operator in ('+', '-', '*', '/', '//', '%', '**'):
    operation = f'{float1} {operator} {float2}' 
    result = calculate(float1, float2, operator)
    print(prompt(f'{operation} = {result}'))
