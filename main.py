from bs4 import BeautifulSoup
import requests
import time
import os
import threading
import json
import csv
#def printit():
 #   threading.Timer(5.0,printit).start() 
 #   print("hola")



#printit()
def printit():    
    threading.Timer(5.0,printit).start() 
    url = 'https://www.cronista.com/MercadosOnline/dolar.html'

    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    monedaData=[]

    MonedaRows = page_content.find_all("tr")
    MonedasDict ={}
    for row in MonedaRows[1: ]:
        valoresHtml = row.find_all("td")[1: 3]
        valoresArray =  list(map(lambda data: (data.text), valoresHtml))
        typesHtml = row.find_all()

        name = str(row.find("a").text).strip()
        x=float(str(valoresArray[0][2:7]).replace(",","."))
        y=float(str(valoresArray[1][2:7]).replace(",","."))
        #print(name,valoresArray)
        MonedasDict=[
            [name,str(x),str(y)],
        ]
        #MonedasDict[str(name)]={
        #    "compra": x,
        #    "venta": y
        #}
        
        print(MonedasDict)

 
printit()

