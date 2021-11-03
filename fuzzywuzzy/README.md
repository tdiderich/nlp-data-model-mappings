# Using Fuzzy Matching

## Output - basic_ip_test.py

* keys tested -> ["src_ip", "dstIp", "client_ip", "device_ip"]
* options -> ["srcDevice_ip", "device_ip", "dstDevice_ip"]

```
--- Running Tests On `src_ip` ---
Ratio: srcDevice_ip - Ratio: 67
Partial Ratio: srcDevice_ip - Ratio: 67
Token Set Ratio: srcDevice_ip - Ratio: 67
Token Sort Ratio: srcDevice_ip - Ratio: 67
Process: ('srcDevice_ip', 67)

--- Running Tests On `dstIp` ---
Ratio: dstDevice_ip - Ratio: 47
Partial Ratio: dstDevice_ip - Ratio: 60
Token Set Ratio: dstDevice_ip - Ratio: 59
Token Sort Ratio: dstDevice_ip - Ratio: 59
Process: ('dstDevice_ip', 59)

--- Running Tests On `client_ip` ---
Ratio: srcDevice_ip - Ratio: 57
Partial Ratio: device_ip - Ratio: 71
Token Set Ratio: srcDevice_ip - Ratio: 57
Token Sort Ratio: srcDevice_ip - Ratio: 57
Process: ('srcDevice_ip', 57)

--- Running Tests On `device_ip` ---
Ratio: device_ip - Ratio: 100
Partial Ratio: device_ip - Ratio: 100
Token Set Ratio: device_ip - Ratio: 100
Token Sort Ratio: device_ip - Ratio: 100
Process: ('device_ip', 100)
```

### Understanding
* src_ip 
    - all correct - same scores
* dstIp 
    - all correct 
    - partial ratio scored the highest (unsure if that matters)
* client_ip 
    - only partial ratio was correct - although the rest had the second best option 
    - using all methods together wouldn't necessarily work better in this case 
* device_ip 
    - all correct - same scores

## Output - challenging_ip_test.py

* keys tested -> ["Event.IP", "EventData.srcIp", "EventData.dst_ip", "foo.bar.client_ip", "foo.bar.device_ip", "destination_ip"]
* options -> ["srcDevice_ip", "device_ip", "dstDevice_ip"]

```
--- Running Tests On `Event.IP` ---
Ratio: device_ip - Ratio: 24
Partial Ratio: srcDevice_ip - Ratio: 25
Token Set Ratio: device_ip - Ratio: 59
Token Sort Ratio: device_ip - Ratio: 59
Process: ('device_ip', 59)

--- Running Tests On `EventData.srcIp` ---
Ratio: srcDevice_ip - Ratio: 30
Partial Ratio: srcDevice_ip - Ratio: 33
Token Set Ratio: device_ip - Ratio: 42
Token Sort Ratio: device_ip - Ratio: 42
Process: ('device_ip', 42)

--- Running Tests On `EventData.dst_ip` ---
Ratio: dstDevice_ip - Ratio: 43
Partial Ratio: dstDevice_ip - Ratio: 50
Token Set Ratio: dstDevice_ip - Ratio: 43
Token Sort Ratio: dstDevice_ip - Ratio: 43
Process: ('device_ip', 48)

--- Running Tests On `foo.bar.client_ip` ---
Ratio: srcDevice_ip - Ratio: 48
Partial Ratio: srcDevice_ip - Ratio: 58
Token Set Ratio: srcDevice_ip - Ratio: 48
Token Sort Ratio: srcDevice_ip - Ratio: 48
Process: ('device_ip', 50)

--- Running Tests On `foo.bar.device_ip` ---
Ratio: device_ip - Ratio: 69
Partial Ratio: device_ip - Ratio: 100
Token Set Ratio: srcDevice_ip - Ratio: 69
Token Sort Ratio: device_ip - Ratio: 100
Process: ('device_ip', 90)

--- Running Tests On `destination_ip` ---
Ratio: dstDevice_ip - Ratio: 54
Partial Ratio: dstDevice_ip - Ratio: 50
Token Set Ratio: dstDevice_ip - Ratio: 54
Token Sort Ratio: dstDevice_ip - Ratio: 54
Process: ('dstDevice_ip', 54)
```

### Understanding - challenging_ip_test.py

* src_ip 
    - all correct - same scores
* dstIp 
    - all correct 
    - partial ratio scored the highest (unsure if that matters)
* client_ip 
    - only partial ratio was correct - although the rest had the second best option 
    - using all methods together wouldn't necessarily work better in this case 
* device_ip 
    - all correct - same scores

