import pandas as pd

idades = [17,33,44,22,44,66,77] 

series_idades =  pd.Series(idades)

media_idades = series_idades.describe()
print('Media:', media_idades)