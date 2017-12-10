# -*- coding: utf-8 -*-

from trainer.morphological_analysis.mecab_backend import MecabBackend
class MorphologicalAnalysis():

    def __init__(self, backend):
        self._backend = backend


    def parse(self, string):
        if self._backend == "mecab":
            MecabBackend.parse(string)
