# Python Calculator


def calculate_again():
    # Keep asking until the user provides a valid yes/no response.
    while True:
        answer = input("Do you want to calculate again? (yes/no): ").lower()

        if answer == "yes":
            return True

        elif answer == "no":
            return False

        else:
            print("Please enter yes or no!")


while True:
    operator = input("Enter an operator (+ - * /): ")

    # Validate each number separately so invalid input does not stop the calculator.
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break

        except ValueError:
            print("Please enter a valid number!")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break

        except ValueError:
            print("Please enter a valid number!")

    if operator == "+":
        result = num1 + num2
        print(f"Result: {round(result, 2)}")

    elif operator == "-":
        result = num1 - num2
        print(f"Result: {round(result, 2)}")

    elif operator == "*":
        result = num1 * num2
        print(f"Result: {round(result, 2)}")

    elif operator == "/":
        # Prevent a ZeroDivisionError before performing the division.
        if num2 == 0:
            print("Cannot divide by zero!")
            continue

        else:
            result = num1 / num2
            print(f"Result: {round(result, 2)}")

    else:
        print(f"{operator} is not a valid operator!")

    # End the program when the user chooses not to perform another calculation.
    if not calculate_again():
        print("Thank you for using the calculator!")
        break
