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
      
      print(Fore.RESET +"Ingrese las URLs de los juegos separadas por comas o espacios, o escríbalas todas juntas sin separación alguna:")
      urljuego = input().strip() + ","
      
      def separar_enlaces(enlaces):
            enlaces_separados = enlaces.split("https")
            enlaces_juntos = ",".join(["https" + enlace for enlace in enlaces_separados if enlace])
            return enlaces_juntos
      url_juegos_separadas = (separar_enlaces(urljuego)).split(",")

      print("\033[0;37;40m" + "-" * 120)

      j = 1
      repeticiones = 0
      while j < len(url_juegos_separadas):
            urljuegodata= url_juegos_separadas [j-1].split("/")
            appid= urljuegodata[4]

            store_doc = requests.get("https://store.steampowered.com/api/appdetails?appids="+appid+"&cc=ars&filters=price_overview")
            storesoup = BeautifulSoup(store_doc.content,"html.parser")
            strstoresoup = str(storesoup)

            storejsonprecio = json.loads(strstoresoup)                                        
            strprecio = storejsonprecio[appid]["data"]["price_overview"]["final_formatted"]  
            preciodeljuego = float((strprecio.replace("ARS$","")).replace(",","."))

            market_doc1 = requests.get("https://www.steamcardexchange.net/index.php?gamepage-appid-"+appid)
            marketsoup1 = BeautifulSoup(market_doc1.content, "html.parser")

            num_cartas  = 0
            start_time = time.time()
            while num_cartas == 0:
                  if time.time() - start_time >= 30:
                        print(Fore.RED + "No se pudo obtener el numero de cromos del juego " + urljuegodata[5] + ". En consecuencia, se ignorará y se procederá con el siguiente.")
                        j += 1
                        break
                  
                  market_doc2 = requests.get("https://steamcommunity.com/market/search?q=&category_753_Game%5B%5D=tag_app_"+appid+"&category_753_cardborder%5B%5D=tag_cardborder_0&category_753_item_class%5B%5D=tag_item_class_2&appid=753")
                  marketsoup2 = BeautifulSoup(market_doc2.content, "html.parser")
                  num_cartas_element = marketsoup2.find(id="searchResults_total")
                  if num_cartas_element is not None:
                        num_cartas_texto = num_cartas_element.get_text()
                        num_cartas  = int(num_cartas_texto)
                  else:
                        table = marketsoup1.find('table', {'class': 'game-stats'})
                        num_cartas_element = table.find('th').text.strip() if table else None
                        if num_cartas_element is not None:
                              num_cartas = int(num_cartas_element)
                        else: 
                              time.sleep(1)


            if num_cartas %2==0 :
                  num_drops = num_cartas /2
            if num_cartas %2==1:
                  num_drops = (num_cartas /2)+0.5

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
                  if Contador<=num_cartas  :
                   urlprecio += "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid+"-"+nombre.text+ "separar"


            vectorurl = urlprecio.split("separar")
            Numerodevectores = len(vectorurl)
            floatvector = int(Numerodevectores)
            
            for i in range(0,floatvector-1):
                  
                  time.sleep(0.1)
                  jsonget = requests.get(vectorurl[i])
                  soupprecio = BeautifulSoup(jsonget.content, 'html.parser')
                  jsonprecio = json.loads(str(soupprecio))
                  try:
                        strprecio = jsonprecio["lowest_price"].replace("ARS$ ","")
                  except:
                        strprecio = "0"
                        erroresprecio += 1
                        urlerror += vectorurl[i]+" "

                  str2precio = strprecio.replace(",",".")
                  precio = float(str2precio)

                  if precio != 0:
                   preciomasalto = max(precio, preciomasalto)
                   preciomasbajo = min(precio, preciomasbajo)
                   sumadeprecios += precio
            
            if str(preciomasbajo)=="99999":
                  repeticiones += 1
                  if repeticiones == 3:  
                         print(Fore.RED + "No se pudo procesar el juego " + urljuegodata[5] + ". En consecuencia, se ignorará y se procederá con el siguiente.")
                         print("\033[0;37;40m" + "-" * 120)
                         j += 1
                         repeticiones = 0
                  continue       

            print(Fore.RESET + "El juego\033[1;37;40m "+urljuegodata[5]+ "\033[0;37;40m cuesta: \033[1;37;40m"+ Fore.GREEN + "ARS$ " + str(preciodeljuego)) 
            print(Fore.RESET + "Cantidad de cromos: " + num_cartas_texto)

            min_sell_price = round(float(preciomasbajo) * num_drops, 2)
            min_profit = round(min_sell_price - preciodeljuego, 2)
            
            if float(preciomasbajo) * num_drops > preciodeljuego and (float(preciomasbajo) * num_drops - preciodeljuego) > 1.0:
                  Diferencia = round(float(preciomasalto) - float(preciomasbajo), 2)
                  print(f"Mayor valor: {Fore.GREEN}ARS$ {preciomasalto}{Fore.RESET} // Menor valor: {Fore.RED}ARS$ {preciomasbajo}{Fore.RESET} // Diferencia: {Fore.LIGHTCYAN_EX}ARS$ {Diferencia}")
                  print(f"{Fore.RESET}Vendiendo los cromos se obtiene como mínimo: {Fore.GREEN}ARS$ {min_sell_price}")
                  print(f"{Fore.LIGHTGREEN_EX}PROFIT MÍNIMO: ARS$ {min_profit}")
            elif float(preciomasbajo) * num_drops > preciodeljuego and 0 < (float(preciomasbajo) * num_drops - preciodeljuego) < 1:
                  print(f"{Fore.RED}POCA GANANCIA")
                  print(f"{Fore.RESET}Mayor valor: {Fore.GREEN}ARS$ {preciomasalto}{Fore.RESET} // Menor valor: {Fore.RED}ARS$ {preciomasbajo}{Fore.RESET}")
                  print(f"{Fore.RESET}Vendiendo los cromos se obtiene como mínimo: {Fore.GREEN}ARS$ {min_sell_price}")
                  print(f"{Fore.YELLOW}Ganancia mínima: ARS$ {min_profit}")
            else:
                  print(f"{Fore.RED}SIN GANANCIA")
                  print(f"{Fore.RESET}Mayor valor: {Fore.GREEN}ARS$ {preciomasalto}{Fore.RESET} // Menor valor: {Fore.RED}ARS$ {preciomasbajo}{Fore.RESET}")
                  print(f"{Fore.RESET}Vendiendo los cromos se obtiene como mínimo: {Fore.GREEN}ARS$ {min_sell_price}")
                  print(f"{Fore.RED}Ganancia mínima: ARS$ {min_profit}")

            print("\033[0;37;40m" + "-" * 120)
            repeticiones = 0
            j += 1