n = int(input("Whats your number?: "))
sumOrProduct = input("Sum or product?: ")
output = 0

if sumOrProduct.lower() == "sum":
    for x in range(1, n + 1):
        output += x
elif sumOrProduct.lower() == "product":
    output = 1

    for x in range(1, n + 1):
        output *= x

print(output)