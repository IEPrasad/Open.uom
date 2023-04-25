import sys

# List to store calculation history
history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(e)

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

def select_op(choice):
    global history
    
    if choice == '#':
        return -1
    elif choice == '$':
        # Clear history and return 0
        history.clear()
        return 0
    elif choice == '?':
        # Show calculation history
        if not history:
            print("No past calculations to show")
        else:
            print("Calculation history:")
            for i, calculation in enumerate(history):
                print( calculation)
    elif choice in ('+', '-', '*', '/', '^', '%'):
        while True:
            num1s = input("Enter first number: ")
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1

            try:
                num1 = float(num1s)
                break
            except ValueError:
                print("Not a valid number, please enter again")
                continue

        while True:
            num2s = input("Enter second number: ")
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:
                num2 = float(num2s)
                break
            except ValueError:
                print("Not a valid number, please enter again")
                continue

        result = 0.0
        last_calculation = ""
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)
        else:
            print("Something went wrong")

        last_calculation = f"{num1} {choice} {num2} = {result}"
        print(last_calculation)
        history.append(last_calculation)

    else:
        print("Unrecognized operation")

while True:
    print("Select operation.")
    print("1.Add      : +")
    print("2.Subtract : -")
    print("3.Multiply : *")
    print("4.Divide   : /")
    print("5.Power    : ^")
    print("6.Remainder: %")
    print("7.Terminate: #")
    print("8.Reset    : $")
    print("8.History  : ?")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        sys.exit()


#### very important code