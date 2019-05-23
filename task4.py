import json
import create_ticket as ct
import requests
controller='devnetapi.cisco.com/sandbox/apic_em'
key = ct.response.json()["response"]["serviceTicket"]
print (key)
def gethostcount(token):
    url = "https://" + controller + "/api/v1/network-device/count"
    header = {"content-type": "application/json", "X-Auth-Token":token}
    response = requests.get(url, headers=header, verify=False)
    return response.json()["response"]

count = gethostcount(key)
print("host number:",count)