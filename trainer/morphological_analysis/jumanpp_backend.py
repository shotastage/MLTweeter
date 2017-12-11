# -*- coding: utf-8 -*-

from pyknp import Jumanpp
import re
import os


def parse(line):
    if line == None:
        return
    if line == "\n":
        return

    jumanpp = Jumanpp()
    
    replaced = re.sub('\n|\u3000| ', '', line)
    result = jumanpp.analysis(replaced)

    words = []

    for mrph in result.mrph_list():

        if not mrph == None:
            print('{0}                読み: {1}  品詞: {2}  活用1: {3}  活用2: {4}'.format(mrph.midasi, mrph.yomi, mrph.hinsi, mrph.katuyou1, mrph.katuyou2))
            words.append(mrph.midasi)

    return words
