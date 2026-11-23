import pandas as pd


nomes = ['Jhonatas','Beatriz'] ## dados de nomes
idades = [19,18] ## dados de idades


nomes_idades_dataframe = pd.DataFrame() ## um DataFrame para criar colunas e colocar Series nessas colunas

nomes_series = pd.Series(nomes) ## Series de nomes
idades_series = pd.Series(idades) ## Sries de idades


nomes_idades_dataframe['Nomes'] = nomes_series ## criando a tabela Nomes e adicionando uma Series de nomes a ela
nomes_idades_dataframe['Idades'] = idades_series ## criando a tabela Idades e adicionando uma Series de Idades a ela


print(nomes_idades_dataframe) 
print(f'Summary: {nomes_idades_dataframe.describe()}') ## extraindo informações básica do DataSet que está no DataFrame
