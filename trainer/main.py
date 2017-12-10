from morphological_analysis.mecab_backend import MecabBackend


if __name__ == "__main__":
    
    parsing = MecabBackend()
    print(parsing.parse("もうまじやばい"))