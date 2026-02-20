from netmiko import ConnectHandler

routers = {
    "device_type": "cisco_ios",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345"
}

net_connect = ConnectHandler(**routers)

def ospf_process(process_id, network_address, wildcard_mask, area):
    config_commands = [
        f"router ospf {process_id}",
        f"network {network_address} {wildcard_mask} area {area}"
    ]

    net_connect.send_config_set(config_commands)

process_id = input("Enter OSPF process ID: ")
network_address = input("Enter network address: ")
wildcard_mask = input("Enter wildcard mask: ")
area = input("Enter OSPF area: ")

ospf_process(process_id, network_address, wildcard_mask, area)

net_connect.disconnect()

print("OSPF has been configured successfully.")