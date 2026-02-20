from netmiko import ConnectHandler

switch_details = {
    "device_type": "cisco_ios",
    "host": "10.10.20.40",
    "username": "admin",
    "password": "RG!_Yw200"
}

connection = ConnectHandler(**switch_details)
connection.enable()

print("Device is reachable via SSH")

interfaces = connection.send_command("sh int sta")
print(interfaces)