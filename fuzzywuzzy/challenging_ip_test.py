from fuzzy.fuzzy import Fuzzy

if __name__ == "__main__":
    fuzzy = Fuzzy()
    keys = ["Event.IP", "EventData.srcIp", "EventData.dst_ip", "foo.bar.client_ip", "foo.bar.device_ip", "destination_ip"]
    options = ["srcDevice_ip", "device_ip", "dstDevice_ip"]
    for key in keys:
        print(f'\n--- Running Tests On `{key}` ---')
        fuzzy.runRatioTest(key=key, options=options)
        fuzzy.runParialRatioTest(key=key, options=options)
        fuzzy.runTokenSortRatioTest(key=key, options=options)
        fuzzy.runTokenSetRatioTest(key=key, options=options)
        fuzzy.runProcessTest(key=key, options=options)