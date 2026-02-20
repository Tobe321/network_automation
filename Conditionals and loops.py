devices = {"R1":"IOS", "R2":"IOS-XR", "R3":"IOS-XE"}

node = input()

if node in devices:
    print (f"I can configure {devices[node]}")
else:
    print('I dont know much about these devices')