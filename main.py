import requests
import json

def obtener_token():
    url = "https://10.10.20.14/api/aaaLogin.json"

    body = {
        "aaaUser" : {
            "attributes": {
                "name": "admin",
                "pwd": "C1sco12345"
            }
        }
    }
    cabecera = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False)
    token = respuesta.json()['imdata'][0]['aaaLogin']['attributes']['token']
    return token

token = obtener_token()

print(token)