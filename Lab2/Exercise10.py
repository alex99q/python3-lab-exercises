def fibonacci(num, num2):
    sum = num + num2
    num = num2
    num2 = sum
    print(sum)
    if sum < 200:
        fibonacci(num, num2)


print("1" + "\n" + "1")
fibonacci(1, 1)