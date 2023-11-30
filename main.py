
day_input   = input("Type desired day (1 - 25): ")
day_num     = int(day_input)

while day_num < 1 or day_num > 25:
    day_input   = input("False input, please from 1 to 25: ")
    day_num     = int(day_input)

print(f"Your selected day: >{day_num}<")