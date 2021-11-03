from fuzzy.fuzzy import Fuzzy

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

