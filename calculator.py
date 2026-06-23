
import math

history = []

def calculate(expression):
    try:
        expression = expression.replace("^", "**")
        result = eval(expression)
        history.append(f"{expression} = {result}")
        return result
    except Exception:
        return "Invalid expression"

print("=" * 30)
print("🚀 SMART CALCULATOR")
print("=" * 30)
print("Examples:")
print("10 + 5")
print("8 * 7")
print("2 ^ 5")
print("100 / 4")
print("sqrt(25)")
print("Type 'history' to view calculations")
print("Type 'exit' to quit")
print()

while True:
    user_input = input(">>> ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if user_input.lower() == "history":
        print("\nCalculation History:")
        for item in history:
            print(item)
        print()
        continue

    if "sqrt" in user_input:
        try:
            number = float(user_input[5:-1])
            result = math.sqrt(number)
            history.append(f"sqrt({number}) = {result}")
            print(result)
        except:
            print("Invalid input")
    else:
        print(calculate(user_input))
