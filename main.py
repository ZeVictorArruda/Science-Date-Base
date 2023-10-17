from urllib.request import urlopen, urlretrieve, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

url = "https://www.fundamentus.com.br/fii_imoveis.php"
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

req = Request(url, headers=headers)
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

lista = soup.find('table')

if (lista == None):
    print ('Lista som daddos')
else:
    print('Com dados') 

qtd = soup.findAll('tr', class_='row')
qtd = range(int(len(qtd)-1))

resumo = []

papel =  lista.find('td').getText()
pesquisa = lista.find('td').findNext('td').contents[0]
 
for i in qtd:
    
    acoes = {}
    
    FII = pesquisa.findNext('td').contents[0]
    IMOVEL = FII.findNext('td').contents[0] 
    ENDERECO = IMOVEL.findNext('td').contents[0] 
    CARAC = ENDERECO.findNext('td').contents[0]  
    
    acoes['ID'] = papel
    acoes['FII'] = FII
    acoes['Imovel']= IMOVEL
    acoes['Enrereço'] = ENDERECO
    acoes['Caracteristicas'] = CARAC
    
    resumo.append(acoes)
    
    try:
        papel = CARAC.findNext('td').span.a.contents[0]
        pesquisa = papel.findPrevious('td').findNext('td').contents[0]
    except HTTPError as e:
        print(e.status, e.reason)   
         
dataset = pd.DataFrame(resumo)
dataset.head(10000)
print(dataset)    