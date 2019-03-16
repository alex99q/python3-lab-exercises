leap_years = []

current_year = 2018
while len(leap_years) < 20:
    current_year += 1

    if current_year % 4 != 0:
        continue
    elif current_year % 100 != 0:
        leap_years.append(current_year)
    elif current_year % 400 != 0:
        continue
    else:
        leap_years.append(current_year)

for year in leap_years:
    print(year)