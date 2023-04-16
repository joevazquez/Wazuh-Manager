# Python 3.9
from typing import Any # Variable importada para hacer uso del tipo de variable "Any"
import requests # Librería para realizar las peticiones a la API de Wazuh
import json # Librería para manejar las respuestas que otorga la API.
from collections import Counter # Módulo importado para realizar cuenta de las repeticiones de vulnerabilidades.
from operator import itemgetter # Módulo empleado para tomar un elemento o su puntero.

# Configuración de la conexión
protocol = 'https'
host = 'localhost' # Se coloca la IP si el servidor no está alojado en el local.
port = 55000 # Puerto sugerido por Wazuh
url = f'{protocol}://{host}:{port}'

def top_n_vulnerabilities(n: int, request_header: dict) -> list[tuple[Any, int]]:
    """Función que devuelve el top n de vulnerabilidades más comunes.

    Args:
        n (int): Número entero hasta el que se busca obtener el top
        request_header (dict): Encabezado con el token para hacer correctamente la solicitud

    Returns:
        list[tuple[Any, int]]: Lista con elemento tupla donde se indica el elemento y la cantidad de repeticiones que tuvo.
    """
    response = requests.get(url + "/vulnerability", headers=request_header)
    # Se filtra por "data" de acuerdo a la información que se indica en la documentación de la API.
    vulnerabilities = json.loads(response.text)["data"]
    
    # Counter recibe un iterador, por lo que se tiene que generar filtrando del total de vulnerabilidades.
    vul_count = Counter([vulnerability["cve"] for vulnerability in vulnerabilities])
    
    return vul_count.most_common(n)

def top_n_agents(n: int, request_header: dict) -> list[dict]:
    """Devuelve el top n de agentes con más vulnerabilidades.

    Args:
        n (int): Número entero hasta el que se desea hacer el top
        request_header (dict): Encabezado con el token para hacer correctamente la solicitud

    Returns:
        list[dict]: Lista con los agentes y su total de vulnerabilidades en formato diccionario.
    """
    response = requests.get(url + "/agents", headers=request_header)
    # Debido a que se buscan los agentes con vulnerabilidades, se filtra por elementos afectados.
    agents = json.loads(response.text)["data"]["affected_items"]
    
    agent_vulnerabilities = []
    for agent in agents:
        # Acceso a las vulnerabilidades por agente
        vul_response = requests.get(url + f"/vulnerability/{agent}", headers=request_header)
        vulnerabilities = json.loads(vul_response.text)["data"] # Filtro para visualizar únicamente la información relevante.
        total_vul = len(vulnerabilities)
        agent_vulnerabilities.append({"agent" : agent, "vulnerabilities" : total_vul})
    # Se ordena descendentemente la lista con la llave "vulnerabilities" del diccionario
    return sorted(agent_vulnerabilities, key=itemgetter("vulnerabilities"), reverse=True)[:n]

def get_configuration(request_header: dict)->json:
    """Funcion que devuelve la configuración actual del servidor de Wazuh

    Args:
        request_header (dict): Encabezado con el token para hacer correctamente la solicitud
        
    Returns:
        json: Formato de cadena de json que posee la configuración del servidor
    """
    response = requests.get(url + "/manager/configuration", headers=request_header)
    configuration = json.loads(response.text)["data"]
    
    # Se regresa en formato json-string para su próximo manejo
    return json.dumps(configuration, indent=4)

def get_logs(request_header: dict)->json:
    """Función que devuelve los registros del servidor de Wazuh

    Args:
        request_header (dict): Encabezado con el token para hacer correctamente la solicitud
        
    Returns:
        json: Formato de cadena de json que posee los registros del servidor.
    """
    response = requests.get(url + "/manager/logs", headers=request_header)
    # El json en "data" contiene los siguientes campos:
    #   total_affected_items
    #   failed_items
    #   total_failed_items
    #   affected_items
    logs = json.loads(response.text)["data"]
    return json.dumps(logs, indent=4)

def get_log_summary(request_header: dict)->json:
    """Función que devuelve un sumario de los registros del servidor de Wazuh

    Args:
        request_header (dict): Encabezado con el token para hacer correctamente la solicitud
    
    Returns:
        json: Formato de cadena de json que posee el sumario de los registros del servidor.
    """
    response = requests.get(url + "/manager/logs/summary",  headers=request_header)
    # Son bastantes campos los que devuelve el json, con un máximo de los últimos 2000 registros
    log_summary = json.loads(response.text)["data"]
    
    return json.dumps(log_summary, indent=4)

def print_functions(response_list: list, operation: int, n: int = None):
    """Función que permite mostrar el resultado de las operaciones que se hacen con la API

    Args:
        response_list (list): lista procesada con los elementos requeridos de acuerdo a la función que ejecutan
        operation (int): De acuerdo a la operación que se realice se indica el índice
        n (int, optional): Si se desea mostrar un top, es el número n que se buscó. Predeterminado en None.
    """
    # Diccionario de evaluación para el tipo de operación que se pase
    conditions = {
        (operation == 1) : "Vulnerabilidades por criticidad",
        (operation == 2) : "Vulnerabilidades por palabra clave",
        (operation == 4) : "Equipos con vulnerabilidad en común",
        (operation == 5) : f"Top {n} de vulnerabilidades más comunes", 
        (operation == 6) : f"Top {n} de agentes con más vulnerabilidades",
    }
    print(conditions.get(True, "Operación desconocida"))
    if(operation == 5 or operation == 6):
        for idx, (element, count) in enumerate(response_list):
            print(f"{idx+1}. {element} con {count} repeticiones")
    else:
        for item in response_list:
            print(item)
    return None
            
        