import time
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
hoje = int(today.strftime("%d"))

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
driver.find_element_by_xpath('//*[@id="sap-user"]').send_keys(loginSAP)
driver.find_element_by_xpath('//*[@id="sap-password"]').send_keys(senhaSAP)
driver.find_element_by_xpath('//*[@id="LOGON_BUTTON"]').click()
time.sleep(5)
# Clicando na barra de tranzação (dentro de iframe)
driver.switch_to.frame("ITSFRAME1")
# Acessando sq01
aguardarElemento('//*[@id="ToolbarOkCode"]').send_keys('mb51')
aguardarElemento('//*[@id="ToolbarOkCode"]').send_keys(Keys.ENTER)
time.sleep(5)
aguardarElemento('//*[@id="M0:46:::3:34"]').send_keys('PA04')
aguardarElemento('//*[@id="M0:46:::7:34"]').send_keys('101')
aguardarElemento('//*[@id="M0:46:::14:34"]').send_keys(f'{hoje-1}.{mes}.20{ano}')
aguardarElemento('//*[@id="M0:46:::14:59"]').send_keys(f'{hoje-1}.{mes}.20{ano}')
aguardarElemento('//*[@id="M0:37::btn[8]"]').click()
time.sleep(10)
aguardarElemento('//*[@id="cua2sapmenu_btn"]').send_keys(Keys.F9)
aguardarElemento('//*[@id="M1:46:2:1::1:0-txt"]').click()
aguardarElemento('//*[@id="M1:37::btn[0]"]').click()
aguardarElemento('//*[@id="M1:46:::1:12"]').send_keys(r'BDProducaoD-1.CSV')
aguardarElemento('//*[@id="M1:37::btn[11]"]').click()
time.sleep(60)



