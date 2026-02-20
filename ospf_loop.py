from netmiko import ConnectHandler
import yaml

with open("routers.yaml") as file:
    data = yaml.safe_load(file)

routers = data["routers"]

def ospf_process(net_connect, process_id, network_address, wildcard_mask, area):
    config_commands = [
        f"router ospf {process_id}",
        f"network {network_address} {wildcard_mask} area {area}"
    ]

    net_connect.send_config_set(config_commands)

process_id = input("Enter OSPF process ID: ")
network_address = input("Enter network address: ")
wildcard_mask = input("Enter wildcard mask: ")
area = input("Enter OSPF area: ")

for router in routers:
    print(f"Connecting to {router['name']} ({router['host']})")
    netmiko_router = router.copy()
    netmiko_router.pop("name")

    net_connect = ConnectHandler(**netmiko_router)

print("OSPF configuration completed on all routers.")

