

def better_calculator():
    while True:
        try:
            number1 = float(input("Please type your first number: "))
            number2 = float(input("Please type your second number: "))
            operation = input("What operation would you like to use? 1 for +, 2 for -, 3 for * and 4 for %: ")
            if operation.isnumeric():
                operation = int(operation)

                if operation == 1:
                    result = number1 + number2
                    print(str(number1), " + ", str(number2), " is ", str(result))
                elif operation == 2:
                    result = number1 - number2
                    print(str(number1), " + ", str(number2), " is ", str(result))
                elif operation == 3:
                    result = (number1 * number2)
                    print(str(number1), " times ", str(number2), " is ", str(result))
                elif operation == 4:
                    result = number1 / number2
                    remainder = number1 % number2
                    print(str(number1), " divided by ", str(number2), " is ", str(result), " with a remainder of  ", str(remainder))
                else:
                    print("Invalid operation")

                cont = input("Would you like to continue? yes/no: ")
                cont.lower()
                if cont != "yes":
                    break
            else:
                print("Invalid operation")

        except ValueError:
            print("That is not a number")

better_calculator()
