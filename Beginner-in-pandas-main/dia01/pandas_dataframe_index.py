import pandas as pd

nomes = ['Jhonatas','Beatriz']
idades = [19,18]

nomes_series = pd.Series(nomes)
idade_series = pd.Series(idades)

nomes_idades_dataframe = pd.DataFrame()

nomes_idades_dataframe['Nomes'] =  nomes_series
nomes_idades_dataframe['Idades'] = idade_series

print(nomes_idades_dataframe.iloc[0]) ## isso me retorna uma series, em que os nomes das colunas viram o index dos intens

print(nomes_idades_dataframe.iloc[0]['Idades']) ## logo posso acessar um item de um data frame pelo indice posicional e pelo index da series retornada no [0]
print(nomes_idades_dataframe.iloc[1]['Idades'])