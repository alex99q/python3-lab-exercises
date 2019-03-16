num = int(input("Your number: "))

factorial = 1
while num > 0:
    factorial *= num

    num -= 1

print(factorial)