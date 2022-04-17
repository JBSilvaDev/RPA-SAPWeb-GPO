from pathlib import Path
import os
import time

local = Path('./').absolute()
print(local)

print("Deletando arquivos antigos...")
print("=" * 30)

# Deleta arquivos CSV
try:
    print('BDEstoque deletado!')
    os.unlink(f'{local}\ArquivosCSV\BDEstoque.csv')
except:
    pass
try:
    print('BDFaturamentoD-1 deletado!')
    os.unlink(f'{local}\ArquivosCSV\BDFaturamentoD-1.csv')
except:
    pass
try:
    print('BDFaturamentoMes deletado!')
    os.unlink(f'{local}\ArquivosCSV\BDFaturamentoMes.csv')
except:
    pass
try:
    print('BDProducaoD-1 deletado!')
    os.unlink(f'{local}\ArquivosCSV\BDProducaoD-1.csv')
except:
    pass
try:
    print('Report deletado!')
    os.unlink(f'{local}\ArquivosCSV\Report.csv')
    print("=" * 30)
except:
    pass
print("=" * 30)
print("Iniciando importação de arquivos...")
print("=" * 30)
# Baixa novos arquivos (CSV)
print('Carregando faturamento dia anterior')
time.sleep(10)
try:
    print("=" * 30)
    print("Importando dados do faturamento D-1")
    print("=" * 30)
    import Faturamento_dia_anterior_SAP
except:
    print("=" * 30)
    print("Falha ao importar dados do faturamento D-1")
    print("=" * 30)
    pass
print('Carregando faturamento do mês')
time.sleep(10)
try:
    print("=" * 30)
    print("Importando faturamento do mês")
    print("=" * 30)
    import Faturamento_mes_SAP
except:
    print("=" * 30)
    print("Falha ao importar faturamento do mês")
    print("=" * 30)
    pass
print('Carregando saldo estoque porto')
time.sleep(10)
try:
    print("=" * 30)
    print("Importando saldo atual GPO")
    print("=" * 30)
    import Importando_Saldo_GPO
except:
    print("=" * 30)
    print("Falha ao importar dados do GPO")
    print("=" * 30)
    pass
print('Carregando saldo estoque fábrica')
time.sleep(10)
try:
    print("=" * 30)
    print("Importando saldo de armazéns fábrica")
    print("=" * 30)
    import Importando_Saldo_SAP
except:
    print("=" * 30)
    print("Falha ao importar saldo de armazéns")
    print("=" * 30)
    pass
print('Carregando produção dia anterior')
time.sleep(10)
try:
    print("=" * 30)
    print("Importando produção D-1")
    print("=" * 30)
    import Produzido_dia_anterior
except:
    print("=" * 30)
    print("Falha ao importar dados da produção D-1")
    print("=" * 30)
    pass