from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class Fuzzy:

    def runRatioTest(self, key: str, options: list):
        winner = ""
        ratio = 0
        for option in options:
            newRatio = fuzz.ratio(key, option)
            if newRatio > ratio:
                winner = option
                ratio = newRatio

        print(f'Ratio: {winner} - Ratio: {ratio}')

    def runParialRatioTest(self, key: str, options: list):
        winner = ""
        ratio = 0
        for option in options:
            newRatio = fuzz.partial_ratio(key, option)
            if newRatio > ratio:
                winner = option
                ratio = newRatio
        
        print(f'Partial Ratio: {winner} - Ratio: {ratio}')
    
    def runTokenSortRatioTest(self, key: str, options: list):
        winner = ""
        ratio = 0
        for option in options:
            newRatio = fuzz.token_sort_ratio(key, option)
            if newRatio > ratio:
                winner = option
                ratio = newRatio
        
        print(f'Token Set Ratio: {winner} - Ratio: {ratio}')

    def runTokenSetRatioTest(self, key: str, options: list):
        winner = ""
        ratio = 0
        for option in options:
            newRatio = fuzz.token_set_ratio(key, option)
            if newRatio > ratio:
                winner = option
                ratio = newRatio
        print(f'Token Sort Ratio: {winner} - Ratio: {ratio}')
    
    def runProcessTest(self, key: str, options: list):
        winner = process.extractOne(key, options)
        print(f'Process: {winner}')