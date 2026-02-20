def ospf_process (process_id, network_address, wildcard_mask, area):
    ospf = print(f"router ospf {process_id}",
          f"network {network_address} {wildcard_mask} area {area}")

print(ospf)
ospf_process ("1" , "192.168.10.1", "0.0.0.255", "0")
