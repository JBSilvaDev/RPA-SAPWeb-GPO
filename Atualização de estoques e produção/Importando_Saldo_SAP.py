import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from login import loginSAP, senhaSAP


local = Path('./').absolute()


#Funcão para aguardar elementos
def aguardarElemento (elemento):
    aguarde = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,elemento)))
    return aguarde

chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
localdownload = {"download.default_directory": f'{local}\ArquivosCSV'}
chrome_options.experimental_options["prefs"]= localdownload
driver = webdriver.Chrome(options=chrome_options)

# Acessando SAP WEB
driver.get("Link SAPWEB")

time.sleep(5)
# Fazendo Login
aguardarElemento('//*[@id="sap-user"]').send_keys(loginSAP)
aguardarElemento('//*[@id="sap-password"]').send_keys(senhaSAP)
aguardarElemento('//*[@id="LOGON_BUTTON"]').click()
time.sleep(5)

# Clicando na barra de tranzação (dentro de iframe)
driver.switch_to.frame("ITSFRAME1")
# Acessando LX02
aguardarElemento('//*[@id="ToolbarOkCode"]').send_keys('LX02')
aguardarElemento('//*[@id="ToolbarOkCode"]').send_keys(Keys.ENTER)
# Preenchendo infomações
aguardarElemento('//*[@id="M0:46:::0:34"]').send_keys('004')
aguardarElemento('//*[@id="M0:46:::1:34"]').send_keys('CES')
aguardarElemento('//*[@id="M0:46:::14:34"]').send_keys('/julianobs')
aguardarElemento('//*[@id="M0:46:::14:34"]').send_keys(Keys.F8)
time.sleep(10)
aguardarElemento('//*[@id="cua2sapmenu_btn"]').send_keys(Keys.F9)
time.sleep(5)
aguardarElemento('//*[@id="M1:46:2:1::1:0-txt"]').click()
aguardarElemento('//*[@id="M1:46:2:1::1:0-txt"]').click()
aguardarElemento('//*[@id="M1:37::btn[0]"]').click()
aguardarElemento('//*[@id="M1:46:::1:12"]').send_keys(r"BDEstoque.CSV")
aguardarElemento('//*[@id="M1:37::btn[11]"]').click()

time.sleep(2)
#driver.save_screenshot('sss.png')
# Fechando Navegador

