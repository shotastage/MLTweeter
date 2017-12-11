from morphological_analysis.mecab_backend import MecabBackend
from morphological_analysis.jumanpp_backend import parse

if __name__ == "__main__":
    

    chars = []
    with open("../ignore/new_sample.txt", "r") as parse_target:
        lines = parse_target.readlines()


        print("----------- 形態素解析開始 -----------")
        for line in lines:
            chars.append(parse(line))
        print("----------- 解析終了 -----------")

    print(chars)

    with open("save.txt", "a") as save:
        save.readlines(chars)
