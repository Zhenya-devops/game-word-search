from typing import List, Dict
from convert import Convert

import pymorphy2


class Analysis:
    def __init__(self):
        self.__morph = pymorphy2.MorphAnalyzer()
        self.__converter = Convert()

    def __morphological_analysis_world(self, word: str) -> List:
        result = self.__morph.parse(word)[0]
        return [word.lower(), result.tag.POS]

    def __morphological_analysis_world_with_converter(self, word: str) -> List:
        result = self.__morph.parse(word)[0]
        return [word.lower(), self.__converter.get_convert_to_guess(result.tag.POS)]

    def morphological_analysis_world(self, word: str):
        return self.__morphological_analysis_world(word)

    def morphological_analysis_text(self, text: str) -> List:
        list_analysis: list = []
        for word in text.split():
            list_analysis.append(f"{self.__morphological_analysis_world(word)[0]}_"
                                 f"{self.__morphological_analysis_world(word)[1]}")
        return list_analysis

    def morphological_analysis_text_and_converter(self, text: str) -> List:
        list_analysis: list = []
        for word in text.split():
            list_analysis.append(f"{self.__morphological_analysis_world_with_converter(word)[0]}_"
                                 f"{self.__morphological_analysis_world_with_converter(word)[1]}")
        return list_analysis
