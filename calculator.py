class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        try:
            result = x + y
            self.history.append(f"{x} + {y} = {result}")
            return result
        except TypeError:
            return "Error: invalid types. Please enter numbers only."
        except Exception as e:
            return f"Error: an unexpected error occurred. {str(e)}"

    def subtract(self, x, y):
        try:
            result = x - y
            self.history.append(f"{x} - {y} = {result}")
            return result
        except TypeError:
            return "Error: invalid types. Please enter numbers only."
        except Exception as e:
            return f"Error: an unexpected error occurred. {str(e)}"

    def multiply(self, x, y):
        try:
            result = x * y
            self.history.append(f"{x} * {y} = {result}")
            return result
        except TypeError:
            return "Error: invalid types. Please enter numbers only."
        except Exception as e:
            return f"Error: an unexpected error occurred. {str(e)}"

    def divide(self, x, y):
        try:
            if y == 0:
                raise ValueError("Error: cannot divide by zero.")
            result = x / y
            self.history.append(f"{x} / {y} = {result}")
            return result
        except TypeError:
            return "Error: invalid types. Please enter numbers only."
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"Error: an unexpected error occurred. {str(e)}"

    def print_history(self):
        for i, calculation in enumerate(self.history, 1):
            print(f"{i}. {calculation}")


calculator = Calculator()

while True:
    operation = input("Enter operation (+, -, *, /, h for history, q to quit): ").strip()
    if operation == "q":
        break
    elif operation in ("+", "-", "*", "/"):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if operation == "+":
            result = calculator.add(x, y)
        elif operation == "-":
            result = calculator.subtract(x, y)
        elif operation == "*":
            result = calculator.multiply(x, y)
        elif operation == "/":
            result = calculator.divide(x, y)
        print(f"Result: {result}")
    elif operation == "h":
        calculator.print_history()
    else:
        print("Invalid operation. Please try again.")
