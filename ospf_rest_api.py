import requests
from requests.auth import HTTPBasicAuth
import urllib3 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

router_ip = "10.10.20.48"
username = "developer"
password = "C1sco12345"

base_url = f"https://{router_ip}"

url = f"{base_url}/restconf/data/Cisco-IOS-XE-ospf-oper:ospf-oper-data"

headers = {
    "Accept": "application/yang-data+json"
}

try:
    response = requests.get(
        url,
        headers=headers,
        auth=HTTPBasicAuth(username, password),
        verify=False,
        timeout=10
    )

    if response.status_code == 200:
        print("Connection to router was successful")

        data = response.json()

        ospf_states = data.get("ospf-oper-data", {}).get("ospf-state", [])

        if not ospf_states:
            print("No OSPF process found")
        else:
            for process in ospf_states:
                process_id = process.get("process-id")
                router_id = process.get("router-id")

                print(f"OSPF Process ID: {process_id}")
                print(f"Router ID: {router_id}")
                print("_" * 30)

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Error connecting to the router:")
    print(e)