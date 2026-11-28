import pandas as pd
import lxml


#coletando dados
dataset = pd.read_html("https://webscraper.io/test-sites/tables/tables-semantically-correct")

#encontrando a tabela
print(dataset[1])

table_web = dataset[1]

table_web.to_csv("/home/jota/Documentos/Pandas_learning/Beginner-in-pandas-main/data/table_web.csv")




