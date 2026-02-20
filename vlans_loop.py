from netmiko import ConnectHandler
import yaml 

switch_details = {
    "device_type": "cisco_ios",
    "host": "10.10.20.40",
    "username": "admin",
    "password": "RG!_Yw200",
    "secret": "RG!_Yw200"
}

try:
    with open("vlans.yaml") as file:
        vlan_data = yaml.safe_load(file)
    connection = ConnectHandler(**switch_details)
    connection.enable()

    for vlan in vlan_data["vlans"]:
        commands = [
            f"vlan {vlan['id']}",
            f"name {vlan['name']}"
        ]
        connection.send_config_set(commands)

    output = connection.send_command("sh vlan br")
    print(output)

    connection.disconnect()

except Exception as e:
    print(f"Error occured: {e}")

