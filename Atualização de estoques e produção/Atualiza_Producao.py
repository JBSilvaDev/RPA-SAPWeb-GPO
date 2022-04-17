
import pandas as pd
from pathlib import Path

local = Path('./').absolute()



#Consulta BDEstoque
try:
    BD_Producao = pd.read_csv(f'{local}\ArquivosCSV\BDProducaoD-1.csv', sep = '\t', encoding='UTF-8', header=1)
    BD_Producao.columns = BD_Producao.columns.str.strip()
    BD_Producao['Linha Producao'] = ''
    BD_Producao = BD_Producao[['Data doc.', 'Lote', 'Linha Producao']]
except:
    BD_Producao = pd.read_csv(f'{local}\ArquivosCSV\BDProducaoD-1.csv', sep = '\t', encoding='latin1', header=1)
    BD_Producao.columns = BD_Producao.columns.str.strip()
    BD_Producao['Linha Producao'] = ''
    BD_Producao = BD_Producao[['Data doc.', 'Lote', 'Linha Producao']]
for i, item in enumerate(BD_Producao['Lote']):
    if 'S1' in str(item):
        BD_Producao['Linha Producao'][i] = 'L1'
    elif 'S2' in str(item):
        BD_Producao['Linha Producao'][i] = 'L2'
BD_Producao = BD_Producao[['Lote', 'Linha Producao']].groupby(['Linha Producao']).count()

BD_Producao = BD_Producao.reset_index()

producaoL1 = 0
producaoL2 = 0

for index, linhas in enumerate(BD_Producao['Linha Producao']):
    if 'L1' in str(linhas) or 'L2' in str(linhas):
        if 'L1' in str(linhas):
            producaoL1 = int(BD_Producao['Lote'][index])* 2
        elif 'L2' in str(linhas):
            producaoL2 = int(BD_Producao['Lote'][index])* 2
    else:
        pass
producaoTotal = producaoL2 + producaoL1
#print(producaoTotal)






