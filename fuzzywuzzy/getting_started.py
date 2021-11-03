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

if __name__ == "__main__":
    fuzzy = Fuzzy()
    keys = ["src_ip", "dstIp", "client_ip", "device_ip"]
    options = ["srcDevice_ip", "device_ip", "dstDevice_ip"]
    for key in keys:
        print(f'\n--- Running Tests On `{key}` ---')
        fuzzy.runRatioTest(key=key, options=options)
        fuzzy.runParialRatioTest(key=key, options=options)
        fuzzy.runTokenSortRatioTest(key=key, options=options)
        fuzzy.runTokenSetRatioTest(key=key, options=options)
        fuzzy.runProcessTest(key=key, options=options)

