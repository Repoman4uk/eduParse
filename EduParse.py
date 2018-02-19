import json
from bs4 import BeautifulSoup
import requests




httpAddress = input("Введите ссылку на образовательный сайт: ")

tableFile = open("table.json", "r")

tableString = tableFile.read()

table = json.loads(tableString)

for l in table["links"]:
    link = l["link"]
    print("Проверка раздела " + l["description"])
    page = requests.get(httpAddress + link)
    pageText = page.text
    soup = BeautifulSoup(pageText, "html.parser")
    commonAttrCount = len(l["props"])
    print("Число проверяемых атрибутов : " + str(commonAttrCount))
    existedAttrCount = 0
    for prop in l["props"]:
        attrs = []
        attrs = soup.find_all(attrs = {"itemprop" : prop}, recursive = True)
        if len(attrs) == 0:
            title = prop[0].upper() + prop[1:]
            attrs = soup.find_all(attrs = {"itemprop" : title}, recursive = True)
        if len(attrs) > 0:
            existedAttrCount += 1
            print("Атрибут itemprop = " + prop + " существует")
        else:
            print('Атрибут itemprop = ' + prop + " НЕ существует")
    print("Найдено атрибутов : " + str(existedAttrCount))
