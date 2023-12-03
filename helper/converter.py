class Converter:
    __input_list = list()

    def __init__(self, day, part) -> None:
        self.file = open("input_data/day" + day + "_" + part + ".txt", "r")
        
        for line in self.file:
            line = line.strip()
            self.__input_list.append(line)

        self.file.close()

    def get_input_list(self) -> list:
        return self.__input_list

    def print_file(self) -> None:
        print(self.input_list)