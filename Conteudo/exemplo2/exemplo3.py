import pandas as pd
import numpy as np

try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]

    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()

    print(df_roubo_veiculo.head())
    print('\nDados obtidos com sucesso')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()


try:
    print('\nCalculando informações sobre padrão de roubo de veículos...')
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia_media_mediana_roubo = abs((media_roubo_veiculo - mediana_roubo_veiculo)/mediana_roubo_veiculo)#*100
    
    print(f'Media de roubo de veiculos: {media_roubo_veiculo}')
    print(f'Mediana de roubo de veiculos: {mediana_roubo_veiculo}')
    print(f'Diferenca entre media e mediana: {distancia_media_mediana_roubo}')
          
except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()