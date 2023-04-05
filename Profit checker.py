from bs4 import BeautifulSoup
from colorama import Fore, init
import requests
import json
import time
import base64
from os import system


init(convert=True)
system("cls")
print(Fore.GREEN + base64.b64decode( b'CiAvJCQkJCQkJCAgICAgICAgICAgICAgICAgICAgICAvJCQkJCQkICAvJCQgICAvJCQgICAgICAgICAgICAgICAgICAgICAKfCAkJF9fICAkJCAgICAgICAgICAgICAgICAgICAgLyQkX18gICQkfF9fLyAgfCAkJCAgICAgICAgICAgICAgICAgICAgIAp8ICQkICBcICQkIC8kJCQkJCQgICAvJCQkJCQkIHwgJCQgIFxfXy8gLyQkIC8kJCQkJCQgICAgICAgICAgICAgICAgICAgCnwgJCQkJCQkJC8vJCRfXyAgJCQgLyQkX18gICQkfCAkJCQkICAgIHwgJCR8XyAgJCRfLyAgICAgICAgICAgICAgICAgICAKfCAkJF9fX18vfCAkJCAgXF9fL3wgJCQgIFwgJCR8ICQkXy8gICAgfCAkJCAgfCAkJCAgICAgICAgICAgICAgICAgICAgIAp8ICQkICAgICB8ICQkICAgICAgfCAkJCAgfCAkJHwgJCQgICAgICB8ICQkICB8ICQkIC8kJCAgICAgICAgICAgICAgICAgCnwgJCQgICAgIHwgJCQgICAgICB8ICAkJCQkJCQvfCAkJCAgICAgIHwgJCQgIHwgICQkJCQvICAgICAgICAgICAgICAgICAKfF9fLyAgICAgfF9fLyAgICAgICBcX19fX19fLyB8X18vICAgICAgfF9fLyAgIFxfX18vICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAvJCQkJCQkICAvJCQgICAgICAgICAgICAgICAgICAgICAgICAgICAvJCQgICAgICAgICAgICAgICAgICAgICAgICAgIAogLyQkX18gICQkfCAkJCAgICAgICAgICAgICAgICAgICAgICAgICAgfCAkJCAgICAgICAgICAgICAgICAgICAgICAgICAgCnwgJCQgIFxfXy98ICQkJCQkJCQgICAvJCQkJCQkICAgLyQkJCQkJCR8ICQkICAgLyQkICAvJCQkJCQkICAgLyQkJCQkJCAKfCAkJCAgICAgIHwgJCRfXyAgJCQgLyQkX18gICQkIC8kJF9fX19fL3wgJCQgIC8kJC8gLyQkX18gICQkIC8kJF9fICAkJAp8ICQkICAgICAgfCAkJCAgXCAkJHwgJCQkJCQkJCR8ICQkICAgICAgfCAkJCQkJCQvIHwgJCQkJCQkJCR8ICQkICBcX18vCnwgJCQgICAgJCR8ICQkICB8ICQkfCAkJF9fX19fL3wgJCQgICAgICB8ICQkXyAgJCQgfCAkJF9fX19fL3wgJCQgICAgICAKfCAgJCQkJCQkL3wgJCQgIHwgJCR8ICAkJCQkJCQkfCAgJCQkJCQkJHwgJCQgXCAgJCR8ICAkJCQkJCQkfCAkJCAgICAgIAogXF9fX19fXy8gfF9fLyAgfF9fLyBcX19fX19fXy8gXF9fX19fX18vfF9fLyAgXF9fLyBcX19fX19fXy98X18vICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA=').decode())
while (True):
    opcion = 1
    if opcion ==1:
      print(Fore.WHITE + "Ingrese las url de los juegos (separadas entre: , )")
      urljuego = input()+","
      urljuego2=urljuego.split(",")
      Numerosdejuegos= len(urljuego2)
      for j in range(1,Numerosdejuegos):

            urljuegodata= urljuego2[j-1].split("/")
            appid= urljuegodata[4]

            store_doc = requests.get("https://store.steampowered.com/api/appdetails?appids="+appid+"&cc=ars&filters=price_overview")
            storesoup= BeautifulSoup(store_doc.content,"html.parser")
            strstoresoup= str(storesoup)
            storejsonprecio= json.loads(strstoresoup)                                        
            strprecio= storejsonprecio[appid]["data"]["price_overview"]["final_formatted"]  

            print("El juego\033[1;37;40m "+urljuegodata[5]+ "\033[0;37;40m cuesta: \033[1;37;40m"+ Fore.GREEN + strprecio +"\033[0;37;40m")

            precioreplace= strprecio.replace("ARS$","")
            precioreplace2= precioreplace.replace(",",".")
            preciodeljuego= float(precioreplace2)

            market_doc1 = requests.get("https://www.steamcardexchange.net/index.php?gamepage-appid-"+appid)

            marketsoup1 = BeautifulSoup(market_doc1.content, "html.parser")

            market_doc2 = requests.get("https://steamcommunity.com/market/search?q=&category_753_Game%5B%5D=tag_app_"+appid+"&category_753_cardborder%5B%5D=tag_cardborder_0&category_753_item_class%5B%5D=tag_item_class_2&appid=753")

            marketsoup2 = BeautifulSoup(market_doc2.content, "html.parser")

            numerosdecartas = marketsoup2.find(id="searchResults_total")
            Ncartas=numerosdecartas.get_text()
            Cartas=int(Ncartas)
            print("Cantidad de cromos: " + Ncartas)

            if Cartas%2==0 :
                  Dropcartas=Cartas/2
            if Cartas%2==1:
                  Dropcartas=(Cartas/2)+0.5


            urlprecio=""
            jsonget=""
            strprecio=""
            precios=""
            urlerror=""
            preciomasalto=0
            preciomasbajo=99999
            sumadeprecios=0
            Numerodevectores=0
            Contador=0
            erroresprecio=0

            for nombre in marketsoup1.findAll("span", attrs={"class":"element-text"}):
                  Contador+=1
                  if Contador<=Cartas :
                   urlprecio += "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid+"-"+nombre.text+ "separar"


            vectorurl = urlprecio.split("separar")
            Numerodevectores= len(vectorurl)
            floatvector = int(Numerodevectores)
            
            
            for i in range(0,floatvector-1):
                  
                  time.sleep(0.1)

                  jsonget = requests.get(vectorurl[i])
                  soupprecio =BeautifulSoup(jsonget.content, 'html.parser')
                  soupstrprecio= str(soupprecio)
                  jsonprecio= json.loads(soupstrprecio)
                  try:
                        strprecio= jsonprecio["lowest_price"].replace("ARS$ ","")
                  except:
                        strprecio="0"
                        erroresprecio+=1
                        urlerror+=vectorurl[i]+" "

                  str2precio= strprecio.replace(",",".")
                  precio= float(str2precio)

                  if precio !=0 :
                        if preciomasalto<precio:
                              preciomasalto=precio

                        if preciomasbajo>precio:
                              preciomasbajo=precio

                        sumadeprecios+= precio
                  
            if float(preciomasbajo)*Dropcartas>preciodeljuego and (float(preciomasbajo)*Dropcartas-preciodeljuego) > 1.0:
                 Diferencia=float(preciomasalto)-float(preciomasbajo)
                 Diferencia= round(Diferencia,2)
                 Diferencia2= (preciomasalto)/float(preciomasbajo)
                 Diferencia2= round(Diferencia2,2)
                 print("Mayor valor: "+ Fore.GREEN + "ARS$ " + str(preciomasalto)+Fore.RESET+ " // Menor valor: "+ Fore.RED + "ARS$ " + str(preciomasbajo)+Fore.RESET+" // Diferencia: "+ Fore.LIGHTCYAN_EX + "ARS$ " + str(Diferencia))
                 print(Fore.RESET + "Vendiendo los cromos se obtiene como minimo: "+ Fore.GREEN + "ARS$ " + str(float(preciomasbajo)*Dropcartas))
                 resultado = round(float(preciomasbajo)*Dropcartas-preciodeljuego, 2)
                 print(Fore.GREEN + "PROFIT MINIMO: " + "ARS$ " + str(resultado))
            else:
                 print(Fore.RED + "PERDIDA O POCA GANANCIA")
                 print(Fore.RESET + "Mayor valor: "+ Fore.GREEN + "ARS$ " + str(preciomasalto)+Fore.RESET+ " // Menor valor: "+ Fore.RED + "ARS$ " + str(preciomasbajo)+Fore.RESET)
                 print(Fore.RESET + "Vendiendo los cromos se obtiene como minimo: "+ Fore.GREEN + "ARS$ " + str(float(preciomasbajo)*Dropcartas))
                 resultado = round(float(preciomasbajo)*Dropcartas-preciodeljuego, 2)
                 print(Fore.RED + "Ganancia minima: "+ "ARS$ " + str(resultado))
            
            print("\033[0;37;40m")
            print("------------------------------------------------------------------------------------------------------------------------")
            print("")
