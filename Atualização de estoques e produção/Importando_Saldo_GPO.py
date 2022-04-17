# Pega informações do porto
import time
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Funcão para aguardar elementos
def aguardarElemento (elemento):
    aguarde = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,elemento)))
    return aguarde

local = Path('./').absolute()

#Deletando CSV antigo
try:
    os.unlink(f'{local}\ArquivosCSV\Report.csv')
except:
    pass

#driver = webdriver.Chrome(executable_path=r'D:/Python/Relatorio Estoque-Producao-Faturado/chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
localdownload = {"download.default_directory": f'{local}\ArquivosCSV'}
chrome_options.experimental_options["prefs"]= localdownload
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.portocel.com.br/gpo/")
time.sleep(1)                        
login = aguardarElemento('/html/body/form/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[2]/input')
time.sleep(1)
login.send_keys('Login')
senha = aguardarElemento('/html/body/form/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/input')
time.sleep(1)
senha.send_keys('Senha')
aguardarElemento('//*[@id="tbrImg"]').click()
time.sleep(2)

driver.get("https://web.portocel.com.br/gpo/paginanotfound")
time.sleep(2)

#Baixar CSV
aguardarElemento('//*[@id="StiViewer_JsViewerMainPanel"]/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div/table/tbody/tr/td[3]/img').click()
aguardarElemento('/html/body/form/div/div/div/div[14]/div/div[11]/table/tbody/tr/td[2]').click()
aguardarElemento('/html/body/form/div/div/div/div[18]/div[4]/table/tbody/tr/td[1]/div/table/tbody/tr/td').click()

time.sleep(15)


