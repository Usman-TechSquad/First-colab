print("=== SIMPLE PYTHON CALCULATOR ===")

while True:
    print("\nChoose an operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("Type 'exit' to quit")

    operator = input("Operation: ")

    if operator.lower() == "exit":
        print("Calculator shutting down...")
        break

    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operation! Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                continue
            result = num1 / num2

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")
