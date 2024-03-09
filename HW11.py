def calculate(num1, num2, action):
    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '*':
        return num1 * num2
    elif action == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "You can't divide by 0"
    else:
        return "Invalid action"

while True:
    num1 = float(input("Please enter first number: "))
    num2 = float(input("Please enter second number: "))
    action = input("Please enter action (+, -, *, /): ")

    result = calculate(num1, num2, action)
    print("Your result is", result)

    answer = input("Do you want to perform another calculation? (yes/no): ")
    if answer.lower() != 'yes' and answer.lower() != 'y':
        break