import requests
import json
import conf

sandbox = "https://10.10.20.14"


def obtener_token(usuario, clave):
    url = "https://10.10.20.14/api/aaaLogin.json"

    body = {
        "aaaUser": {
            "attributes": {
                "name": usuario,
                "pwd": clave
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


# token = obtener_token(conf.usuario, conf.clave)
# GET http://apic-ip-address/api/class/topSystem.json
# http://APIC-IP/api/mo/topology/pod-1/node-101/sys.json
# obtener_token(conf.usuario, conf.clave)
# GET URL: http://APIC-IP/api/mo/uni/tn-TENANT_NAME.json?query-target=subtree&target-subtree-class=fvBD

def top_system():
    cabecera = {
        "Content-Type": "application/json"
    }
    galleta = {
        "APIC-Cookie": obtener_token(conf.usuario, conf.clave)
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.get(sandbox + "/api/class/topSystem.json", headers=cabecera, cookies=galleta, verify=False)
    print(respuesta.json())


def status_node():
    cabecera = {
        "Content-Type": "application/json"
    }
    galleta = {
        "APIC-Cookie": obtener_token(conf.usuario, conf.clave)
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.get(sandbox + "/api/mo/topology/pod-1/node-101/sys.json", headers=cabecera, cookies=galleta,
                             verify=False)
    print(respuesta.json())

def status_bridgedomain():
    cabecera = {
        "Content-Type": "application/json"
    }
    galleta = {
        "APIC-Cookie": obtener_token(conf.usuario, conf.clave)
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.get(sandbox + "/api/mo/uni/tn-Heroes.json?query-target=subtree&target-subtree-class=fvBD",
                             headers=cabecera, cookies=galleta, verify=False)
    print(respuesta.json())

status_bridgedomain()
