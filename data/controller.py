import pandas as pd
from pathlib import Path


class DbFilter:
    def __init__(self):
        self.path = Path('./').resolve().parents[0]

    def sap_balance(self):
      sap_stoke_balance = pd.read_csv(fr'{self.path}\Report-Logistc\Arquivos\BDEstoque.CSV', sep = '\t', encoding='utf-8', header=2)
      sap_stoke_balance = sap_stoke_balance[['Material', 'Dep.', 'Texto breve material', 'Lote', 'PosDepósit']].dropna()
      sap_stoke_balance['Linha'] = ''
      for i, item in enumerate(sap_stoke_balance['Lote']):
          if 'S2' in item:
              sap_stoke_balance['Linha'][i] = 'L2'
          else: 
              sap_stoke_balance['Linha'][i] = 'L1'
      ESTOQUE_TOTAL = len(sap_stoke_balance['Material']) * 2
      TOTAL_PERC = f'{ESTOQUE_TOTAL  / 38000:.0%}'
      EST_L1 = (sap_stoke_balance['Linha'] == 'L1').sum() * 2
      L1_PERC = f'{EST_L1  / 8000:.0%}'
      EST_L2 = (sap_stoke_balance['Linha'] == 'L2').sum() * 2
      L2_PERC = f'{EST_L2  / 30000:.0%}'
      return ESTOQUE_TOTAL, TOTAL_PERC, EST_L1, L1_PERC, EST_L2, L2_PERC
    
    def gpo_balance(self):
      gpo_stoke_balance = pd.read_csv(f'{self.path}\Report-Logistc\Arquivos\Report.csv', sep = ';', encoding='UTF-8')
      gpo_stoke_balance = gpo_stoke_balance[['DatalgReport_COD_MERCADORIA', 'Text3']]
      gpo_stoke_balance = gpo_stoke_balance.rename(columns={'DatalgReport_COD_MERCADORIA': 'Mercadoria'})
      gpo_stoke_balance = gpo_stoke_balance.rename(columns={'Text3': 'Qtde'})
      gpo_stoke_balance['Unidade'] = ''
      for i, item in enumerate(gpo_stoke_balance['Mercadoria']):
          if 'MSP' in item:
              gpo_stoke_balance['Unidade'][i] = 'Mucuri'
          else:
              gpo_stoke_balance['Unidade'][i] = 'Anothers'
      gpo_stoke_balance = gpo_stoke_balance[['Unidade', 'Qtde']].groupby(['Unidade']).sum()
      TOTAL_PORTO = int(f"{gpo_stoke_balance['Qtde'][1] * 2}")
      TOTAL_PERC = f'{(int(TOTAL_PORTO) / 60000):.0%}'
      return TOTAL_PORTO, TOTAL_PERC    
    
    def sap_d_1(self):
      sap_d_1 = pd.read_csv(f'{self.path}\Report-Logistc\Arquivos\BDFaturamentoD-1.csv', sep = '\t', encoding='UTF-8', header=2)
      sap_d_1.columns = sap_d_1.columns.str.strip()
      sap_d_1['Mercado'] = ''
      sap_d_1 = sap_d_1[['Descrição do Cliente', 'Peso bruto', 'Mercado']]
      for i, item in enumerate(sap_d_1['Descrição do Cliente']):
        if item == 'Portocel - Term. Espec. Barra do Ri':
            sap_d_1['Mercado'][i] = 'ME'
            faturado_porto = sap_d_1['Peso bruto'][i]
            sap_d_1['Peso bruto'][i] = int(sap_d_1['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
            #print(f'porto {faturado_porto}')
        elif isinstance(item, float):
            sap_d_1['Mercado'][i] = 'Total'
            total_dia = sap_d_1['Peso bruto'][i]
            sap_d_1['Peso bruto'][i] = int(sap_d_1['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
            #print(f'total dia {total_dia}')
        else:
            sap_d_1['Mercado'][i] = 'MI'
            faturado_mi = sap_d_1['Peso bruto'][i]
            sap_d_1['Peso bruto'][i] = int(sap_d_1['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
        FAT_D_1_MI = 0
        FAT_D_1_ME = 0
        FAT_D_1_TOTAL = 0
      for i, item in enumerate(sap_d_1['Mercado']):
          if item == 'ME':
              FAT_D_1_ME += int(sap_d_1['Peso bruto'][i])
          elif item == 'MI':
              FAT_D_1_MI += int(sap_d_1['Peso bruto'][i])
          else:
              FAT_D_1_TOTAL += int(sap_d_1['Peso bruto'][i])
      return FAT_D_1_MI, FAT_D_1_ME, FAT_D_1_TOTAL
        
    def sap_month(self):
        sap_month = pd.read_csv(f'{self.path}\Report-Logistc\Arquivos\BDfaturamentoMes.csv', sep = '\t', encoding='UTF-8', header=2)
        sap_month.columns = sap_month.columns.str.strip()
        sap_month['Mercado'] = ''
        sap_month = sap_month[['Descrição do Cliente', 'Peso bruto', 'Mercado']]
        for i, item in enumerate(sap_month['Descrição do Cliente']):
            if item == 'Portocel - Term. Espec. Barra do Ri':
                sap_month['Mercado'][i] = 'ME'
                faturado_porto = sap_month['Peso bruto'][i]
                sap_month['Peso bruto'][i] = int(sap_month['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
                #print(f'porto {faturado_porto}')
            elif isinstance(item, float):
                sap_month['Mercado'][i] = 'Total'
                total_dia = sap_month['Peso bruto'][i]
                sap_month['Peso bruto'][i] = int(sap_month['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
                #print(f'total dia {total_dia}')
            else:
                sap_month['Mercado'][i] = 'MI'
                faturado_mi = sap_month['Peso bruto'][i]
                sap_month['Peso bruto'][i] = int(sap_month['Peso bruto'][i].replace('.', '').replace(',', '')) / 1000
                #print(f'MI {faturado_mi}')

        FAT_MES_ME = 0
        FAT_MES_MI = 0
        FAT_MES_TOTAL = 0

        for i, item in enumerate(sap_month['Mercado']):
            if item == 'ME':
                FAT_MES_ME += int(sap_month['Peso bruto'][i])
            elif item == 'MI':
                FAT_MES_MI += int(sap_month['Peso bruto'][i])
            else:
                FAT_MES_TOTAL += int(sap_month['Peso bruto'][i])
        return FAT_MES_ME, FAT_MES_MI, FAT_MES_TOTAL

    def sap_product(self):
        sap_product = pd.read_csv(f'{self.path}\Report-Logistc\Arquivos\BDProducaoD-1.csv', sep = '\t', encoding='UTF-8', header=1)
        sap_product.columns = sap_product.columns.str.strip()
        sap_product['Linha Producao'] = ''
        sap_product = sap_product[['Data doc.', 'Lote', 'Linha Producao']]       
        for i, item in enumerate(sap_product['Lote']):
            if 'S1' in str(item):
                sap_product['Linha Producao'][i] = 'L1'
            elif 'S2' in str(item):
                sap_product['Linha Producao'][i] = 'L2'
        sap_product = sap_product[['Lote', 'Linha Producao']].groupby(['Linha Producao']).count()

        sap_product = sap_product.reset_index()

        PROD_L1 = 0
        PROD_L2 = 0

        for index, linhas in enumerate(sap_product['Linha Producao']):
            if 'L1' in str(linhas) or 'L2' in str(linhas):
                if 'L1' in str(linhas):
                    PROD_L1 = int(sap_product['Lote'][index])* 2
                elif 'L2' in str(linhas):
                    PROD_L2 = int(sap_product['Lote'][index])* 2
            else:
                pass
        PROD_TOTAL = PROD_L1 + PROD_L2
        return PROD_L1, PROD_L2, PROD_TOTAL