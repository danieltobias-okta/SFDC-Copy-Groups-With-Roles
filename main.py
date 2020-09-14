# Python 3.8.5
from requests import *
import json

base_url = ""
api_token = ""
app_id = ""
target_app_id = ""

url = "https://" + base_url

headers = {'Accept' : 'application/json', 'Content-Type':'application/json', 'Authorization' : 'SSWS ' + api_token}

response = get(url + "/api/v1/apps/" + app_id + "/groups?limit=200", headers = headers)

groups_to_reassign = response.json()
print(response.text)

for group in groups_to_reassign:
    body = {'id':group['id'], 'profile' : {'role': group['profile']['role'], 'profile' : group['profile']['profile']}}
    # body = {'id':group['id'], 'profile' : {"orgUnitPath": group['profile']['orgUnitPath'],"manageLicenses": False, "roles": []}}
    data = json.dumps(body)
    response = put(url + "/api/v1/apps/" + target_app_id + "/groups/" + group['id'], headers = headers, data = data)
    print(response.text)

