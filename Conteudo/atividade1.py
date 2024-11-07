from sqlalchemy import create_engine
import pandas as pd
import numpy as np 

host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df_estoque = pd.read_sql('tb_produtos', engine)
print(df_estoque.head())

df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']

df_agrupado = df_estoque.groupby('NomeProduto').agg({
    'QuantidadeEstoque' : 'sum',
    'TotalEstoque' : 'sum'
}).reset_index()

df_ordenado = df_agrupado.sort_values(by='TotalEstoque', ascending=False)

print(df_ordenado{['NomeProduto', 'TotalEstoque']})

# print(df_estoque[['NomeProduto', 'TotalEstoque']])

# print(f'Total geral em estoque: R${df_estoque["TotalEstoque"].sum()}')


# total = df_estoque['TotalEstoque']
# print(total.describe())

# mediana = np.median(df_estoque['TotalEstoque'])
# print(f'\nMediana: {mediana}')

# media = np.mean(df_estoque['TotalEstoque'])
# print(f'Media: {media}')


array_total_estoque = np.array(df_agrupado['TotalEstoque'])

media = np.mean(array_total_estoque)
mediana = np.median(array_total_estoque)


distancia_media_mediana = abs((media - mediana)/mediana)*100
print(f'Media do valor total: {media: .2f}')
print(f'Mediana do valor total: {mediana: .2f}')
print(f'Distânci entre a média e a mediana: {distancia_media_mediana: .2f}')
