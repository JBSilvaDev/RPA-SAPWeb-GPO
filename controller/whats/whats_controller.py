from controller.user_key.key_controller import ControllerLogin
from models.msg_model import MsgModel
import urllib.parse
from selenium import webdriver 
from selenium.webdriver.common.by import By as selectItem 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.alert import Alert
import os 
import time 


path_locate = os.getcwd()
service = Service(ChromeDriverManager().install())

def enable_download(driver):
  print('Driver recebido')
  driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
  params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': f'{path_locate}\Arquivos'}}
  driver.execute("send_command", params)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(r'user-data-dir=C:\Users\username\AppData\Local\Google\Chrome\User Data\Perfil Selenium')
prefsChrome = {
"download.default_directory": f'{path_locate}\Arquivos',
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing.enabled": True, 
}

chrome_options.experimental_options["prefs"] = prefsChrome 
inBrowser = webdriver.Chrome(service=service, options = chrome_options, ) 

controller = ControllerLogin()
controller.find_number_whatsApp()

class WhatsController():

    def __init__(self):
        self.inBrowser = inBrowser
        self.selectItem = selectItem
        self.key = Keys
        self.number = controller.number
        self.link = f'https://wa.me/{self.number}'
        self.msg_model = MsgModel()
        
          
    def open_browser(self):
        self.inBrowser.get(self.link)

    def wait_elements(self, element:str):
        maxLoop = 0
        listElement = self.inBrowser.find_elements(self.selectItem.XPATH, element)
        while len(listElement) < 1 and maxLoop < 600:
            time.sleep(1)
            maxLoop+=1
        time.sleep(1)
        if len(listElement) < 1:
            print('Tempo esgotado, elemento não encontrado')
            return
        return self.inBrowser.find_element(self.selectItem.XPATH, element)
    
    
    def send_messeger(self):
      msg = urllib.parse.quote(self.msg_model.msg_final_zap)
      self.link = f'{self.link}?text={msg}'
      self.open_browser()
      time.sleep(10)
      self.wait_elements('//*[@id="action-button"]/span').click()
      time.sleep(10)
      self.wait_elements('//*[@id="fallback_block"]/div/div/h4[2]/a/span').click()
      time.sleep(15)
      self.wait_elements('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
      time.sleep(5)
      self.inBrowser.quit()



