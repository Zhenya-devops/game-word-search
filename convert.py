from typing import List

from constants import DICT_PART_SPEECH


class Convert:
    def __init__(self):
        self.__text = []

    def __convert_to_list__(self, text: str):
        self.__text = text.split()

    def get_convert_to_list(self, text: str) -> List:
        self.__convert_to_list__(text)
        return self.__text

    @staticmethod
    def __convert_maw_to_guess__(pos: str) -> str:
        return str(DICT_PART_SPEECH.get(pos))

    def get_convert_to_guess(self, pos: str) -> str:
        return self.__convert_maw_to_guess__(pos)
