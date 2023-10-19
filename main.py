import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('acidentes2022.csv', sep=';')

y = dataset.iloc[:, 3].values

acidentes = []

try: 
    for converse in y:
        numero = int(converse)
        acidentes.append(numero)
        
except ValueError:
    print("A conversão não é possível, a string não representa um número inteiro válido.")

semVitimas = 0
comVitimas = 0
fatalVitimas = 0

for numero in acidentes:
    if (numero == 1):
        comVitimas += 1
    if (numero == 2):
        semVitimas += 1      
    if(numero == 3):
        fatalVitimas += 1                
        
print("Acidentes sem vitimas:", semVitimas)
print("Acidentes com vitimas:", comVitimas)
print("Acidentes com vitimas Fatal:", fatalVitimas)

acTotal = semVitimas + comVitimas + fatalVitimas

#Muda a cor das barras pela ordem
cores = ['green','blue','red','black']

#Array com os numeros de acidentes
arrayAcidentes = [semVitimas,comVitimas,fatalVitimas, acTotal]
strings = [
    'Sem Vitimas - '+str(semVitimas),
    'Com Vitimas - '+str(comVitimas),
    'Fatal Vitimas - '+str(fatalVitimas),
    'Total de Vitimas - '+str(acTotal)
    ]

#Criação da tabela estilo barras 
plt.bar(range(len(arrayAcidentes)), arrayAcidentes, color=cores)
plt.title("Acidentes 2022")
plt.ylabel("Números de acidentes")
plt.xticks(range(len(arrayAcidentes)), strings)

# Exiba o gráfico
plt.show()
        
