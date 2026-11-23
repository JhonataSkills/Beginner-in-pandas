import pandas as pd


idades = [19,77,34]
nomes = ['Jota','maira', 'pedro']

## em listas o index não se atrelou ao item 
print(idades)
print(idades[-1])
##idades.sort()
print(idades)
print(idades[-1])


## em series os index são atrelados ao item mas também os itens possuem index de posições  
series_idades = pd.Series(idades,index = nomes)
print(seires_idades)
series_idades_srt = seires_idades.sort_values()
print(series_idades_srt)

## acessando o alemento de uma series pela posição
print(series_idades_srt.loc[-1])
