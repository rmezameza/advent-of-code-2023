from helper.day import Day

class Day1(Day):
    __sum_calibration_values = 0

    def part_one(self) -> any:
        for line in self._Day__input_list_one:
            number_one      = ""
            number_two      = ""

            for char in str(line):
                if char.isdigit():
                    if number_one == "":
                        number_one = char
                    else:
                        number_two = char
            
            if number_two != "":
                self.__sum_calibration_values   += int(number_one + number_two)
            else:
                self.__sum_calibration_values   += int(number_one + number_one)


        return self.__sum_calibration_values

    def part_two(self) -> any:
        return super().part_two()