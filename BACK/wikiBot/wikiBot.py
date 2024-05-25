import requests
class wikiBot:
    def __init__(wikiFamily):
        response = requests.get(url)
        response_json = response.json()
        print(response_json)