from morphological_analysis import parser

try:
    parsing = parser.MorphologicalAnalysis("mecab")
except:
    print("ぁぁぁ")
    
    exit()
try:

    parsing.parse("もうまじやばい")
except:
    print("dk")
