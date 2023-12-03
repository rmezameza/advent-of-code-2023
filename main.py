from days.day1 import Day1

day_input   = input("Type desired day (1 - 1): ")
day_num     = int(day_input)

while day_num < 1 or day_num > 1:
    day_input   = input("False input, please from 1 to 25: ")
    day_num     = int(day_input)

print(f"Welcome to day >{day_num}<")

day1 = Day1()
day1.fill_list(day_input, "1")
print(day1.part_one())
day1.fill_list(day_input, "2")

