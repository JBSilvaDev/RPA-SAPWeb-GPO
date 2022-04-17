import time
import calendar
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from login import loginSAP, senhaSAP

local = Path('./').absolute()


#faturamento do mes
#Funcão para aguardar elementos
def aguardarElemento (elemento):
    aguarde = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,elemento)))
    return aguarde

#Data atual
today = date.today()

#Ano com base na data atual
ano = int(today.strftime("%y"))
#Mes com base na data atual
mes =  int(today.strftime("%m"))
#Dia com base no ano e mes (Mostra o range "quantos dias tem o mes")
final_mes = int(calendar.monthrange(ano, mes)[1])

chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
localdownload = {"download.default_directory": f'{local}\ArquivosCSV'}
chrome_options.experimental_options["prefs"]= localdownload
driver = webdriver.Chrome(options=chrome_options)

# Acessando SAP WEB
driver.get("https://ecphanacls.suzano.com.br:8101/sap/bc/gui/sap/its/webgui?sap-client=500&sap-language=PT")

# Fazendo Login
aguardarElemento('//*[@id="sap-user"]').send_keys(loginSAP)
aguardarElemento('//*[@id="sap-password"]').send_keys(senhaSAP)
aguardarElemento('//*[@id="LOGON_BUTTON"]').click()
time.sleep(5)
# Clicando na barra de tranzação (dentro de iframe)
driver.switch_to.frame("ITSFRAME1")
# Acessando sq01
time.sleep(10)
aguardarElemento('//*[@id="ToolbarOkCode"]').send_keys('sq01')
aguardarElemento('//*[@id="ToolbarOkCode"]').send_keys(Keys.ENTER)

time.sleep(5)
#Click Menu
aguardarElemento('//*[@id="cua2sapmenu_btn"]').click()

#Tentando mudar ambiente para Standart
try:
    #Mouse Ambiente
    elemento = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/div/div/div[2]/span[1]/div/div[2]/table/tbody/tr[6]/td[3]')
    hover = ActionChains(driver).move_to_element(elemento)
    hover.perform()

    time.sleep(2)

    #Mouse Are de trabalho
    elemento2 = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div/div/div/div[2]/span[20]/div/div[2]/table/tbody/tr[1]/td[3]/span').click()
    hover = ActionChains(driver).move_to_element(elemento2)
    hover.perform()
    time.sleep(2)
except:
    pass
#Clicando em standart
aguardarElemento('//*[@id="M1:46:::0:0-txt"]').click()
aguardarElemento('//*[@id="M1:37::btn[2]"]').click()
time.sleep(5)
aguardarElemento('//*[@id="M0:46:::2:21"]').send_keys('SD114')
aguardarElemento('//*[@id="M0:46:::2:21"]').send_keys(Keys.F8)
time.sleep(10)
#Preenchendo informações
aguardarElemento('//*[@id="M0:46:::1:34"]').send_keys('MUCU')
aguardarElemento('//*[@id="M0:46:::2:34"]').send_keys('02')
aguardarElemento('//*[@id="M0:46:::4:34"]').send_keys('CE')
aguardarElemento('//*[@id="M0:46:::4:59"]').send_keys('CE')
aguardarElemento('//*[@id="M0:46:::5:34"]').send_keys(f'{final_mes-final_mes+1}.{mes}.20{ano}')
aguardarElemento('//*[@id="M0:46:::5:59"]').send_keys(f'{final_mes}.{mes}.20{ano}')
aguardarElemento('//*[@id="M0:46:::15:4"]').click()
aguardarElemento('//*[@id="M0:46:::15:34"]').send_keys('/JBESCOAMENT')
time.sleep(1)
aguardarElemento('//*[@id="M0:37::btn[8]"]').click()
#Baixando BD
time.sleep(180)

driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, Keys.SHIFT, Keys.F9)
time.sleep(1)
aguardarElemento('//*[@id="M1:46:2:1::1:0-txt"]').click()
aguardarElemento('//*[@id="M1:37::btn[0]"]').click()
aguardarElemento('//*[@id="M1:46:::1:12"]').send_keys(r"BDFaturamentoMes.CSV")
aguardarElemento('//*[@id="M1:37::btn[11]"]').click()
time.sleep(10)



