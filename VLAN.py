from netmiko import ConnectHandler

switch_details = {
    "device_type": "cisco_ios",
    "host": "10.10.20.40",
    "username": "admin",
    "password": "RG!_Yw200"
}

vlan_commands = [
    f"vlan 10",
    "name SALES",

]

try:
    connection = ConnectHandler(**switch_details)
    connection.enable()

    connection.send_config_set(vlan_commands)

    output = connection.send_command("sh vlan brief")
    print(output)

    connection.disconnect()

except Exception as e:
    print(f"Error: {e}")

