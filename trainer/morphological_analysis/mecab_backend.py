# -*- coding: utf-8 -*-

import MeCab


def parse(string):
    mecab = MeCab.Tagger("-Ochasen")

    return mecab.parse(string)
