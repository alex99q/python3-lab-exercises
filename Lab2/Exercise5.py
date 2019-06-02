range_start = int(input("Beginning of interval: "))
range_end = int(input("End of interval: "))

if range_start < range_end:
    for num in range(range_start, range_end + 1):
        if 0 < num < 10:
            print(num)
            continue
        elif 10 <= num < 100:
            continue
        else:
            power_of_armstrong_num = len(str(num))

            armstrong_num = 0
            for digit in str(num):
                armstrong_num += pow(int(digit), int(power_of_armstrong_num))

            if num == armstrong_num:
                print(armstrong_num)
else:
    print("End of interval can't be higher than beginning of interval")