from netmiko import ConnectHandler

IOS = {
    "device_type": "cisco_ios",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
}
       
net_connect = ConnectHandler(**IOS)
output = net_connect.send_command("show ip int br")
print (output)

net_connect.disconnect