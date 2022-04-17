# Consulta o BDEstoque
import pandas as pd
from pathlib import Path

local = Path('./').absolute()

# Consulta BDEstoque
try:
    BD_estoque = pd.read_csv(f'{local}\ArquivosCSV\BDEstoque.CSV', sep = '\t', encoding='utf-8', header=2)
    #Seleciona Colunas a serem usadas
    BD_estoque = BD_estoque[['Material', 'Dep.', 'Texto breve material', 'Lote', 'PosDepósit']]
    #Deleta colunas vazias
    BD_estoque = BD_estoque.dropna()
    #Adiciona nova coluna
    BD_estoque['Linha'] = ''
except:
    BD_estoque = pd.read_csv(f'{local}\ArquivosCSV\BDEstoque.CSV', sep = '\t', encoding='latin1', header=2)
    #Seleciona Colunas a serem usadas
    BD_estoque = BD_estoque[['Material', 'Dep.', 'Texto breve material', 'Lote', 'PosDepósit']]
    #Deleta colunas vazias
    BD_estoque = BD_estoque.dropna()
    #Adiciona nova coluna
    BD_estoque['Linha'] = ''
#Para cada item na coluna Lote, adicione o conteudo a coluna linha
for i, item in enumerate(BD_estoque['Lote']):
    #Se tiver S2 no conteudo de Lote adicone L2 na coluna Linha
    if 'S2' in item:
        BD_estoque['Linha'][i] = 'L2'
    else: 
        BD_estoque['Linha'][i] = 'L1'
#Conta e Mutiplica os volumes por 2 (2 toneladas cada volume)
estoque_total = len(BD_estoque['Material']) * 2
totalperc = f'{estoque_total  / 38000:.0%}'
#Conta quantos itens existem na L2
estoquel2 = BD_estoque['Linha'] == 'L2'
estoquel2 = estoquel2.sum() * 2
l2perc = f'{estoquel2  / 30000:.0%}'
#Conta quantos itens existem na L1
estoquel1 = BD_estoque['Linha'] == 'L1'
estoquel1 = estoquel1.sum() * 2
l1perc = f'{estoquel1  / 8000:.0%}'

#print(f"{estoquel1} + {estoquel2} + {l1perc} + {totalperc} + {estoque_total}")





