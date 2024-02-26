def calculate(num1, num2, action):
    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '*':
        return num1 * num2
    elif action == '/':
        if num2 != 0:  # Перевірка на ділення на нуль
            return num1 / num2
        else:
            return "You can't divide by 0"
    else:
        return "Invalid action"

num1 = float(input("Please enter first number: "))

num2 = float(input("Please enter second number: "))

action = input("Please enter action: ")

result = calculate(num1, num2, action)
print("Your result is", result)