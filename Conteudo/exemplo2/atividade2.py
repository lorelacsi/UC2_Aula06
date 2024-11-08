import pandas as pd
import numpy as np

try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_estelionato = df_ocorrencias[['mes_ano', 'estelionato']]

    df_estelionato = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()

    print(df_estelionato.head())
    print('\nDados obtidos com sucesso')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

try:

    array_estelionato = np.array(df_estelionato['estelionato'])
    media_estelionato = np.mean(array_estelionato)
    mediana_estelionato = np.median(array_estelionato)
    soma_estelionato = np.sum(array_estelionato)
    distancia_media_mediana_estelionato = abs((media_estelionato - mediana_estelionato)/mediana_estelionato)

    print(f'\nTotal de estelionatos: {soma_estelionato}')
    print(f'Media de estelionatos ocorridos ao longo dos anos: {media_estelionato:.2f}')
    print(f'Mediana de estelionatos ocorridos ao longo dos anos: {mediana_estelionato:.2f}')
    print(f'Diferenca entre media e mediana: {distancia_media_mediana_estelionato:.2f}%')


except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()