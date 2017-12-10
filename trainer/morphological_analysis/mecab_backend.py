# -*- coding: utf-8 -*-

import MeCab

class MecabBackend():

    @staticmethod
    def parse(string):
        mecab = MeCab.Tagger("-Ochasen")
        return mecab.parse(string)