while True:
    # Ask the user to input two numbers and store them as floats
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print()

    # Ask the user to input an operator and store it as a string
    operator = input("Enter operator (+, -, , /): ")

    # Check the operator and perform the corresponding arithmetic operation on the two input numbers
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator")
        continue

    # Print the result of the arithmetic operation
    print("The result is", result)

    # Ask the user whether they want to continue or stop
    choice = input("Do you want to continue? (y/n) ")
    if choice.lower() == 'n':
        break
