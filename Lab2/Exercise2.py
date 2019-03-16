import math

input_num = int(input("Calculate primes to what number?: "))

for n in range(2, input_num + 1):
    m = round(math.sqrt(n))

    is_prime = True
    while m > 1:
        if n % m == 0:
            is_prime = False
            break
        m -= 1

    if is_prime:
        print(n)