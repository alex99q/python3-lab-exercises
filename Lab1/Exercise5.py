n = int(input("Whats your number?: "))
sum = 0

for x in range(1, n + 1):
    if x % 3 == 0 or x % 5 == 0:
        sum = sum + x

print(sum)