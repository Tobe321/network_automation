IP = "172.16.10.1"
#print (dir(IP))

New_IP = IP.replace("172", "192").replace("16","168").replace("10","20")
print (New_IP)