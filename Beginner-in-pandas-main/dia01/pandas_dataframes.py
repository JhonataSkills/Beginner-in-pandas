import pandas as pd

nomes = ['Jhonatas','Beatriz']
idades = [19,18]

nomes_series = pd.Series(nomes)
idade_series = pd.Series(idades)

nomes_idades_dataframe = pd.DataFrame()

nomes_idades_dataframe['Nomes'] =  nomes_series
nomes_idades_dataframe['Idades'] = idade_series

print(nomes_idades_dataframe)
print(f'Summary: {nomes_idades_dataframe.describe()}')