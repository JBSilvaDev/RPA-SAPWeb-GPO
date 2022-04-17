#Consulta o BDfaturamentoMes
import pandas as pd
from pathlib import Path

local = Path('./').absolute()


#Consulta BDEstoque
try:
    BD_FaturamentoMes = pd.read_csv(f'{local}\ArquivosCSV\BDfaturamentoMes.csv', sep = '\t', encoding='UTF-8', header=2)
    BD_FaturamentoMes.columns = BD_FaturamentoMes.columns.str.strip()
    BD_FaturamentoMes['Mercado'] = ''
    BD_FaturamentoMes = BD_FaturamentoMes[['Descrição do Cliente', 'Peso bruto', 'Mercado']]
except:
    BD_FaturamentoMes = pd.read_csv(f'{local}\ArquivosCSV\BDfaturamentoMes.csv', sep = '\t', encoding='latin1', header=2)
    BD_FaturamentoMes.columns = BD_FaturamentoMes.columns.str.strip()
    BD_FaturamentoMes['Mercado'] = ''
    BD_FaturamentoMes = BD_FaturamentoMes[['Descrição do Cliente', 'Peso bruto', 'Mercado']]
for i, item in enumerate(BD_FaturamentoMes['Descrição do Cliente']):
    if item == 'Portocel - Term. Espec. Barra do Ri':
        BD_FaturamentoMes['Mercado'][i] = 'ME'
        faturado_porto = BD_FaturamentoMes['Peso bruto'][i]
        BD_FaturamentoMes['Peso bruto'][i] = int(BD_FaturamentoMes['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
        #print(f'porto {faturado_porto}')
    elif isinstance(item, float):
        BD_FaturamentoMes['Mercado'][i] = 'Total'
        total_dia = BD_FaturamentoMes['Peso bruto'][i]
        BD_FaturamentoMes['Peso bruto'][i] = int(BD_FaturamentoMes['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
        #print(f'total dia {total_dia}')
    else:
        BD_FaturamentoMes['Mercado'][i] = 'MI'
        faturado_mi = BD_FaturamentoMes['Peso bruto'][i]
        BD_FaturamentoMes['Peso bruto'][i] = int(BD_FaturamentoMes['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
        #print(f'MI {faturado_mi}')

faturamentoMesME = 0
faturamentoMesMI = 0
faturamentoMesTotal = 0

for i, item in enumerate(BD_FaturamentoMes['Mercado']):
    if item == 'ME':
        faturamentoMesME += int(BD_FaturamentoMes['Peso bruto'][i])
    elif item == 'MI':
        faturamentoMesMI += int(BD_FaturamentoMes['Peso bruto'][i])
    else:
        faturamentoMesTotal += int(BD_FaturamentoMes['Peso bruto'][i])


#Consulta o BDFaturamentoDia

#Consulta BDEstoque
try:
    BD_FaturamentoD = pd.read_csv(f'{local}\ArquivosCSV\BDFaturamentoD-1.csv', sep = '\t', encoding='UTF-8', header=2)
    BD_FaturamentoD.columns = BD_FaturamentoD.columns.str.strip()
    BD_FaturamentoD['Mercado'] = ''
    BD_FaturamentoD = BD_FaturamentoD[['Descrição do Cliente', 'Peso bruto', 'Mercado']]
except:
    BD_FaturamentoD = pd.read_csv(f'{local}\ArquivosCSV\BDFaturamentoD-1.csv', sep = '\t', encoding='latin1', header=2)
    BD_FaturamentoD.columns = BD_FaturamentoD.columns.str.strip()
    BD_FaturamentoD['Mercado'] = ''
    BD_FaturamentoD = BD_FaturamentoD[['Descrição do Cliente', 'Peso bruto', 'Mercado']]
for i, item in enumerate(BD_FaturamentoD['Descrição do Cliente']):
    if item == 'Portocel - Term. Espec. Barra do Ri':
        BD_FaturamentoD['Mercado'][i] = 'ME'
        faturado_porto = BD_FaturamentoD['Peso bruto'][i]
        BD_FaturamentoD['Peso bruto'][i] = int(BD_FaturamentoD['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
        #print(f'porto {faturado_porto}')
    elif isinstance(item, float):
        BD_FaturamentoD['Mercado'][i] = 'Total'
        total_dia = BD_FaturamentoD['Peso bruto'][i]
        BD_FaturamentoD['Peso bruto'][i] = int(BD_FaturamentoD['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
        #print(f'total dia {total_dia}')
    else:
        BD_FaturamentoD['Mercado'][i] = 'MI'
        faturado_mi = BD_FaturamentoD['Peso bruto'][i]
        BD_FaturamentoD['Peso bruto'][i] = int(BD_FaturamentoD['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
        #print(f'MI {faturado_mi}')

faturamentoDiaME = 0
faturamentoDiaMI = 0
faturamentoDiaTotal = 0

for i, item in enumerate(BD_FaturamentoD['Mercado']):
    if item == 'ME':
        faturamentoDiaME += int(BD_FaturamentoD['Peso bruto'][i])
    elif item == 'MI':
        faturamentoDiaMI += int(BD_FaturamentoD['Peso bruto'][i])
    else:
        faturamentoDiaTotal += int(BD_FaturamentoD['Peso bruto'][i])



