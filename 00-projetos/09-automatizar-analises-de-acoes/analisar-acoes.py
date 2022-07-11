#pip install pandas_datareader
#pip install matplotlib

from pandas_datareader import data as api
import matplotlib.pyplot as plt

#OBTENDO A COTAÇÃO
cotacao_bitcoin = api.DataReader('BTC-USD', data_source='yahoo', start='01-01-2020', end='06-30-2022')
print(cotacao_bitcoin)

#PLOTANDO O GRAFICO
cotacao_bitcoin['Adj Close'].plot()
plt.show()