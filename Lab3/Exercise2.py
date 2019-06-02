def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return None


while True:
    user_input = input("Expression to calculate: ").split()

    if len(user_input) != 3:
        print("Incorrect format!")
        continue

    try:
        num1 = int(user_input[0])
    except:
        print("The first number is not allowed")
        continue

    operator = user_input[1]

    try:
        num2 = int(user_input[2])
    except:
        print("The second number is not allowed")
        continue

    result = calculate(num1, operator, num2)
    if result is None:
        print("The operator is not allowed")
        continue
    else:
        print(result)

    break