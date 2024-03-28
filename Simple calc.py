def main():
    title = "Calculator Application"
    
    # Display this to let users enter a number
    # Needed to add last part to input what were doing with said numbers and what symbols are used for each area
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Reminder: don't forget to add some type of line of code to prevent division by zero
    if operation == '+':
        result = num1 + num2
        operation_name = "sum"
    elif operation == '-':
        result = num1 - num2
        operation_name = "difference"
    elif operation == '*':
        result = num1 * num2
        operation_name = "product"
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        else:
            result = num1 / num2
            operation_name = "quotient"
    else:
        print("Invalid operation. Please enter '+', '-', '*', or '/'.")
        return

    output_message = f"\nThe {operation_name} of {num1} and {num2} is {result}."
    print(output_message)


if __name__ == "__main__":
    main()
