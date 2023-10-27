import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Importa os dados de acidentes
dataset_2021 = pd.read_csv('acidentes2021.csv', sep=';')
dataset_2020 = pd.read_csv('acidentes2020.csv', sep=';')

# Converte a coluna "natureza_acidente" para o formato numérico
dataset_2020['natureza_acidente'] = dataset_2020['natureza_acidente'].replace({
    'SEM ViTIMA': 1,
    'COM VITIMA': 2,
    'VITIMA FATAL': 3,
    'OUTROS': 4
})

dataset_2021['natureza_acidente'] = dataset_2021['natureza_acidente'].replace({
    'SEM ViTIMA': 1,
    'COM VITIMA': 2,
    'VITIMA FATAL': 3,
    'OUTROS': 4
})

x = dataset_2021.iloc[:,-1].values.reshape(-1, 1)
Y = dataset_2021.iloc[:,2].values

X = dataset_2020.iloc[:,-1].values.reshape(-1, 1)
y = dataset_2020.iloc[:,2].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
x_train, x_test, Y_train, Y_test = train_test_split(x, Y, test_size=0.2)

# Cria o modelo de regressão linear
modelo_2020 = LinearRegression()
modelo_2020.fit(X_train, y_train)

modelo_2021 = LinearRegression()
modelo_2021.fit(x_train, Y_train)

# Plota as linhas de regressão
plt.plot(x_test, modelo_2020.predict(x_test), label='2020')
plt.plot(x_test, modelo_2021.predict(x_test), label='2021')

# Adiciona um título e rótulos de eixo ao gráfico
plt.title('Linhas de regressão para dados de acidentes de 2020 e 2021')
plt.xlabel('Ano')
plt.ylabel('Número de acidentes')
plt.legend()

# Limita o eixo x ao intervalo de valores dos dados de treinamento
plt.xlim(x_test.min(), x_test.max())

# Mostra o gráfico
plt.show()