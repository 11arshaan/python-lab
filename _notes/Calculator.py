
# Add
def add(x, y):
    return x + y

# Subtract
def subtract(x, y):
    return x - y

# Multiply
def multiply(x, y):
    return x * y

# Divide
def divide(x, y):
    if y == 0:
        print("divided by 0\n\n")
        return
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    #first num
    num1 = float(input("First number: "))

    #operation
    for symbol in operations:
        print(symbol + " " + operations[symbol].__name__)
    operation = input("Choose an operation from the list above: ")[0]
    while operation not in ["+", "-", "*", "/"]:
            operation = input("Invalid input. Choose an operation + - * /  :   ")[0]

    #second num
    num2 = float(input("Second number: "))

    #answer
    answer = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")

    #loop start
    calc_again = input("Enter y=continue, n=exit, c=clear  :  ").lower()
    while calc_again != "y" and calc_again != "n" and calc_again != "c":
        calc_again = input("Invalid input. Enter y=continue, n=exit, c=clear  :  ").lower()

    while(calc_again == "y"):
        previous_answer = answer
        #operation
        operation = input("Choose an operation  + - * /  :   ")[0]
        while operation not in ["+", "-", "*", "/"]:
            operation = input("Invalid input. Choose an operation + - * /  :   ")[0]

        #second num
        num2 = float(input("New number: "))

        #answer
        answer = operations[operation](previous_answer, num2)
        print(f"{previous_answer} {operation} {num2} = {answer}")

        #repeat
        calc_again = input("Enter y=continue, n=exit, c=clear  :  ").lower()
        while calc_again != 'y' and calc_again != 'n' and calc_again != "c":
            calc_again = input("Invalid input. Enter y=continue, n=exit, c=clear  :  ").lower()

    if(calc_again == "c"): 
        calculator()

calculator()


