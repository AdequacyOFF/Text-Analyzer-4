import requests
class wikiBot:
    def __init__(wikiFamily="https://baza.znanierussia.ru/mediawiki/"):

        tokenUrl = wikiFamily + "api.php?action=query&meta=tokens&format=json" #для получения csrf токена
        response = requests.get(tokenUrl)
        response_json = response.json()
        print (response_json)
        botToken = response_json["query"]["tokens"]["csrftoken"] #получили токен
        print(botToken)

        botLogin = "Stalnoy Voin@textAnalyzerBot" 
        botPassword = "Andrey1Andrey"
        url = wikiFamily+"/api.php?action=login&lgname="+botLogin+"&lgpassword="+botPassword+"&lgtoken="+botToken+"&format=json"
        response = requests.get(url)
        response_json = response.json()
        print(response_json)