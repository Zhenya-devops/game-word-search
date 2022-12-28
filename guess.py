from typing import Dict
from gensim.models import KeyedVectors
from constants import PATH_DICTIONARY


class Guess:
    def __init__(self):
        try:
            self.__model = KeyedVectors.load_word2vec_format(PATH_DICTIONARY, binary=False)
        except FileNotFoundError:
            print('That file already did not exist.')

    def guess_world(self, word_combination: list) -> Dict:
        worlds = []
        for world in word_combination:
            worlds.append(world)

        top_worlds = self.__model.most_similar(positive=worlds, topn=10)
        return dict(top_worlds)
