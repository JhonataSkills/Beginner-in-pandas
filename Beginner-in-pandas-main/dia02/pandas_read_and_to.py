import pandas as pd
import openpyxl
import pyarrow
import fastparquet


##Lendo arquivo xlsx
store_orders = pd.read_excel('/home/jota/Documentos/Pandas_learning/Beginner-in-pandas-main/data/Store_Orders.xlsx')

##Exibindo
print (store_orders)

## Fazendo um parse para csv
store_orders.to_csv('/home/jota/Documentos/Pandas_learning/Beginner-in-pandas-main/data/Store_Orders.csv')

## Exibindo
store_orders_csv = pd.read_csv('/home/jota/Documentos/Pandas_learning/Beginner-in-pandas-main/data/Store_Orders.csv')
print(store_orders_csv)

## Fazendo um parse para Parque
store_orders_csv.to_parquet('/home/jota/Documentos/Pandas_learning/Beginner-in-pandas-main/data/Store_Orders.parquet')

## Exibindo
store_orders_parquet = pd.read_parquet('/home/jota/Documentos/Pandas_learning/Beginner-in-pandas-main/data/Store_Orders.parquet')
print(store_orders_parquet)





