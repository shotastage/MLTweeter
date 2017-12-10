# -*- coding: utf-8 -*-

from morphological_analysis import mecab_backend


class MorphologicalAnalysis():

    def __init__(self, backend):
        self._backend = backend


    def parse(self, string):
        if self._backend == "mecab":
            mecab_backend.parse(string)
