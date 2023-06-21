import requests
import json

url = "https://192.168.152.129/restconf/data/ietf-interfaces:interfaces/interface=Loopback1"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback1",
    "description": "CGDQ",
    "type": "iana-if-type:softwareLoopback",
    "enabled": False,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "1.1.1.1",
          "netmask": "255.255.255.255"
        }
      ]
    }
  }
})
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}

response = requests.request("PUT", url, headers=headers, data=payload, verify=False)

print(response.text)
