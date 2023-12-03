from abc import ABC, abstractmethod
from helper.converter import Converter

class Day(ABC):
    __input_list_one = list()
    __input_list_two = list()

    def fill_list(self, day, part):
        if(part == "1"):
            self.__input_list_one   = Converter(day, part).get_input_list()
        else:
            self.__input_list_two   = Converter(day, part).get_input_list()

    @abstractmethod
    def part_one(self) -> any:
        pass

    @abstractmethod
    def part_two(self) -> any:
        pass