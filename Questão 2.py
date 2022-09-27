import requests
import html5lib
from bs4 import BeautifulSoup

while(True):
    try:
        
        entrada = str(input("Digite o código de 4 caracteres referente ao aeroporto desejado\nou fim caso deseje encerrar o programa\n")).upper()
        if(entrada == "FIM"):
            print("Finalizando!")
            break
        if(len(entrada)!=4):
            raise "erro"
        url = "https://aisweb.decea.mil.br/?i=aerodromos&codigo="+entrada
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html5lib')
        nascer_do_sol = ""
        por_do_sol = ""
        METAR_e_TAF = []
        digitos_horario = [str(i) for i in range(10)]
        digitos_horario.append(":")
        table = soup.find('div', attrs={'class':'col-6 text-right'})
        table = str(table).split('sunrise')[1][1:6]
        nascer_do_sol = table
        table = soup.find('div', attrs={'class':'col-6 text-left'})
        table = str(table).split('sunset')[1][1:6]
        por_do_sol = table
        table = soup.find('div', attrs={'class':'col-lg-4 order-sm-12'})
        info = str(table).split("METAR")[1].split("TAF")[0].replace("</p>","<p>").split("<p>")[1:-1]
        METAR_e_TAF.append(info)
        info = str(table).split("TAF")[1].split("OPEA")[0].replace("</a>","<a>").split("<a>")[1:-1]
        METAR_e_TAF.append(info)
        info = str(table).split("Cartas")[1].split("Rotas Preferenciais")[0].replace("\n","")
        cartas = ""
        i = 0
        flag = ""
        while(i<len(info)):
            if(info[i] == "<" and flag == ""):
                flag += "<"
            elif(flag == "<" and info[i] == "a"):
                flag += "a"
            elif(info[i] == ">" and flag == "<a"):
                flag += ">"
            elif(flag == "<a>" and info[i] != "<"):
                cartas += info[i]
            elif(info[i] == "<" and flag == "<a>"):
                cartas += "\n"
                flag = ""
            i+=1
        
        caracteres = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cartas_lista = cartas.split("\n")
        cartas = ""
        for i in range(len(cartas_lista)):
            for j in caracteres:
                if j in cartas_lista[i]:
                    cartas += cartas_lista[i]+"\n"
                    break
                
        metar = "\n"
        for i in METAR_e_TAF[0]:
            metar += i+"\n"
        taf = "\n"
        for i in METAR_e_TAF[1]:
            taf += i+"\n"
        
        print("\nHorário do nascer do sol de hoje:",nascer_do_sol)
        print("Horário do por do sol de hoje:",por_do_sol+"")
        print("METAR"+metar+"TAF"+taf+"Cartas\n"+cartas)
        
    except:
        print("Código informado é inválido, por favor tente novamente\n")
        continue
    

