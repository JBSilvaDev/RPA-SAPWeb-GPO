import pymsteams
import Import_arquivos
import sys

try:
    import Atualiza_estoque_fabrica
    estoque_total = str(f'{Atualiza_estoque_fabrica.estoque_total:,}').replace(',', '.')
    totalperc = str(Atualiza_estoque_fabrica.totalperc)
except:
    estoque_total = 'Sem Resultados, favor verificar!'
    totalperc = '0%'
try:
    import Atualiza_estoque_porto
    saldoporto = str(f'{Atualiza_estoque_porto.saldoporto:,}').replace(',', '.')
    portoperc = str(f'{Atualiza_estoque_porto.portoperc}')
except:
    saldoporto = 'Sem Resultados, favor verificar!'
    portoperc = '0%'
try:
    import Atualiza_estoque_fabrica
    estoquel1 = str(f'{Atualiza_estoque_fabrica.estoquel1:,}').replace(',', '.')
    l1perc = str(Atualiza_estoque_fabrica.l1perc)
except:
    estoquel1 = 'Sem Resultados, favor verificar!'
    l1perc = '0%'
try:
    import Atualiza_estoque_fabrica
    estoquel2 = str(f'{Atualiza_estoque_fabrica.estoquel2:,}').replace(',', '.')
    l2perc = str(Atualiza_estoque_fabrica.l2perc)
except:
    estoquel2 = 'Sem Resultados, favor verificar!'
    l2perc = '0%'
try:
    import Atualiza_Producao
    producaoL1 = str(f'{Atualiza_Producao.producaoL1:,}').replace(',', '.')
    producaoL2 = str(f'{Atualiza_Producao.producaoL2:,}').replace(',', '.')
    producaoTotal = str(f'{Atualiza_Producao.producaoTotal:,}').replace(',', '.')
except:
    producaoL1 = 'Sem Resultados, favor verificar!'
    producaoL2 = 'Sem Resultados, favor verificar!'
    producaoTotal = 'Sem Resultados, favor verificar!'
try:
    import Atualiza_faturamento_dia_e_mes
    faturamentoDiaME = str(f'{Atualiza_faturamento_dia_e_mes.faturamentoDiaME:,}').replace(',', '.')
    faturamentoDiaMI = str(f'{Atualiza_faturamento_dia_e_mes.faturamentoDiaMI:,}').replace(',', '.')
except:
    try:
        import Atualiza_faturamento_dia_e_mes
        faturamentoDiaME = str(f'{Atualiza_faturamento_dia_e_mes.faturamentoDiaME:,}').replace(',', '.')
        faturamentoDiaMI = str(f'{Atualiza_faturamento_dia_e_mes.faturamentoDiaMI:,}').replace(',', '.')

    except:
        faturamentoDiaME = 'Sem Resultados, favor verificar!'
        faturamentoDiaMI = 'Sem Resultados, favor verificar!'
    pass
try:
    import Atualiza_faturamento_dia_e_mes
    faturamentoMesTotal = str(f'{Atualiza_faturamento_dia_e_mes.faturamentoMesTotal:,}').replace(',', '.')
    faturamentoMesMI = str(f'{Atualiza_faturamento_dia_e_mes.faturamentoMesMI:,}').replace(',', '.')
except:
    faturamentoMesTotal = 'Sem Resultados, favor verificar!'
    faturamentoMesMI = 'Sem Resultados, favor verificar!'




print("Enviando informações para o Teams")
myTeamsMessage = pymsteams.connectorcard("https://SeuLink.com.br/webhook")

myMessageSection = pymsteams.cardsection()

myTeamsMessage.text(" ")
myMessageSection.activityTitle("Titulo da msg")
myMessageSection.activityImage ( "Link de foto para perfil" ) 
myMessageSection.activityText ( "Automation created by: JB Silva!" )

myMessageSection.text("Segue dados sobre estoque faturamento e produção:")

myMessageSection.addFact("Total estoque fábrica =", f"{estoque_total} - ({totalperc})")
myMessageSection.addFact("Total estoque porto =", f"{saldoporto} - ({portoperc})")
myMessageSection.addFact("Total estoque linha 1 =", f"{estoquel1} - ({l1perc})")
myMessageSection.addFact("Total estoque linha 2 =", f"{estoquel2} - ({l2perc})")
myMessageSection.addFact("Produção L1 (D-1) =", f"{producaoL1}")
myMessageSection.addFact("Produção L2 (D-1) =", f"{producaoL2}")
myMessageSection.addFact("Produção Total (D-1) =", f"{producaoTotal}")
myMessageSection.addFact("Faturamento ME (D-1) =", f"{faturamentoDiaME}")
myMessageSection.addFact("Faturamento MI (D-1) =", f"{faturamentoDiaMI}")
myMessageSection.addFact("Faturamento ME MTD =", f"{faturamentoMesTotal}")
myMessageSection.addFact("Faturamento MI MTD =", f"{faturamentoMesMI}")
myTeamsMessage.addSection(myMessageSection)

myTeamsMessage.send()


try:
    raise SystemExit
except:
    sys.exit()
