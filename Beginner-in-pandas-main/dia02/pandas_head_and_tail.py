import pandas as pd

## lendo dataframe
store_orders_parquet = pd.read_parquet('/home/jota/Documentos/Pandas_learning/Beginner-in-pandas-main/data/Store_Orders.parquet')

## exibindo os 5 primeiros itens
print("Os 5 primeiros: \n",store_orders_parquet.head(n=5))

## exibindo os 5 últimos itens
print("Os 5 últimos: \n", store_orders_parquet.tail(n=5))

## exibindo o número de colunas e linhas
print("Número de colunas e linhas: \n",store_orders_parquet.shape)