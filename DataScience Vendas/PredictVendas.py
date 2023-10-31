import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import numpy as np

#pip install openpyxl
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    try:
        tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    except FileNotFoundError:
        print(f'Não há dados disponíveis para o mês de {mes}')
        continue

    nomes = tabela_vendas['Vendedor'].values
    y = tabela_vendas['Vendas'].values
    
    encoder = LabelEncoder()
    nomes_x = encoder.fit_transform(nomes)

    # Separa os dados em dados de treinamento e dados de teste
    X_treino, X_teste, y_treino, y_teste = train_test_split(nomes_x.reshape(-1, 1), y, test_size=0.25)
    
    modelo = LinearRegression()
    modelo.fit(X_treino, y_treino)

    # Faz a previsão das vendas futuras
    y_pred = modelo.predict(X_teste)

    # Calcula a métrica de desempenho
    erro_quadratico_medio = np.mean((y_pred - y_teste)**2)

    # Adiciona uma camada de visualização 

    #plt.bar(nomes,y)  
    #plt.title(f'Vendas de {mes}')
    #plt.xlabel('Vendas previstas')
    #plt.ylabel('Vendas reais')
    #plt.show() 
    
    plt.bar(range(len(y_teste)), y_teste)
    plt.plot(range(len(y_pred)),y_pred, color='r', linestyle='--')
    plt.title(f'Vendas de {mes}')
    plt.xlabel('Vendas previstas')
    plt.ylabel('Vendas reais')
    plt.legend(['Previsto', 'Real'])
    plt.show()
    print(f'Month: {mes}, MSE: {erro_quadratico_medio}')