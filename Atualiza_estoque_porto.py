import pandas as pd
from pathlib import Path

local = Path('./').absolute()


try:
    BDReport = pd.read_csv(f'{local}\ArquivosCSV\Report.csv', sep = ';', encoding='UTF-8')
    #BDReport = BDReport.columns.str.strip()
    BDReport = BDReport[['DatalgReport_COD_MERCADORIA', 'Text3']]
    BDReport = BDReport.rename(columns={'DatalgReport_COD_MERCADORIA': 'Mercadoria'})
    BDReport = BDReport.rename(columns={'Text3': 'Qtde'})
except:
    BDReport = pd.read_csv(f'{local}\ArquivosCSV\Report.csv', sep = ';', encoding='latin1')
    #BDReport = BDReport.columns.str.strip()
    BDReport = BDReport[['DatalgReport_COD_MERCADORIA', 'Text3']]
    BDReport = BDReport.rename(columns={'DatalgReport_COD_MERCADORIA': 'Mercadoria'})
    BDReport = BDReport.rename(columns={'Text3': 'Qtde'})

BDReport['Unidade'] = ''
for i, item in enumerate(BDReport['Mercadoria']):
    if 'MSP' in item:
        BDReport['Unidade'][i] = 'Mucuri'
    else:
        BDReport['Unidade'][i] = 'Anothers'
BDReport = BDReport[['Unidade', 'Qtde']].groupby(['Unidade']).sum()
saldoporto = int(f"{BDReport['Qtde'][1] * 2}")
portoperc = int(saldoporto) / 60000
portoperc = f'{portoperc:.0%}'
#display(BDReport)




