def add(x, y):
    return x + y        

def subtract(x, y): 
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = { '+' : add, '-': subtract, '*': multiply, '/': divide }

def calculator():
    continue_ = True
    num1 = float(input("Enter first number: ")) 
    while continue_ == True:
        for i in operations:
            print(i)
        operation = input("Select operation: ")
        num2 = float(input("Enter second number: "))

        result = round(operations[operation](num1, num2), 2)
        print(f"{num1} {operation} {num2} = {result}")
        if input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            num1 = result
        else:
            if input("Type 'y' to start a new calculation, or type 'n' to exit: ") == 'n':
                continue_ = False
                print("Goodbye")
            else:
                calculator()

calculator()
