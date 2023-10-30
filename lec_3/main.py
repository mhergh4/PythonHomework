
expression = input("Enter an expression: ")

expression = expression.replace(" ", "")  
operators = "+-*/"
operator = None

for op in operators:
    if op in expression:
        operator = op
        num1, num2 = expression.split(op)
        num1, num2 = float(num1), float(num2)
        break

if operator:
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero.")
            result = None
else:
    print("Error: Invalid operator or expression format.")
    result = None

if result is not None:
    print("Result:", result)
