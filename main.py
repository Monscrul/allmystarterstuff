while True:
    try:
        a = input("Type your first number: ")
        b = input("Type your second number: ")
        if a.isnumeric() and b.isnumeric():
                a = float(a)
                b = float(b)
                operation = input("Type x for Addition and y for Subtraction: ")
                if operation == "x":
                    result = a + b
                    print("The answer when added Sis " + str(result))
                elif operation == "y":
                    result = a - b
                    print("The answer when subtracted is " + str(result))
                else:
                    print("Invalid operation, please type valid operation: ")
        else:
            print("Please type valid numbers")

    except ValueError:
        print("That aint no number")
        break
