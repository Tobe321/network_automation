from netmiko import ConnectHandler
import yaml

with open("routers.yaml") as file:
    data = yaml.safe_load(file)

routers = data["routers"]

def ospf_process(ssh, process_id, network_address, wildcard_mask, area):
    ospf_command = [
        f"router ospf {process_id}",
        f"network {network_address} {wildcard_mask} area {area}"
    ]

    ssh.send_config_set(ospf_command)

process_id = input("enter process ID")
network_address = input("enter network address")
wildcard_mask = input("enter wildcard mask")
area = input("enter area")

for router in routers:

    ssh = ConnectHandler(**router)
