from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By as selectItem
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import date, datetime
from selenium.webdriver.common.alert import Alert
import os
import time
import colorama
from colorama import Fore
from colorama import Style


path_locate = r"C:\local\download"
service = Service(ChromeDriverManager().install())


def enable_download(driver):
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": f"{path_locate}\Arquivos"},
    }
    driver.execute("send_command", params)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-dev-shm-usage")
prefsChrome = {
    "download.default_directory": f"{path_locate}\Arquivos",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}

chrome_options.experimental_options["prefs"] = prefsChrome
inBrowser = webdriver.Chrome(
    service=service,
    options=chrome_options,
)


class Controller:
    def __init__(self):
        colorama.init()
        enable_download(inBrowser)
        self.popup = Alert(inBrowser)
        self.inBrowser = inBrowser
        self.selectItem = selectItem
        self.key = Keys
        self.action_chains = ActionChains(self.inBrowser)
        self.ano = int(date.today().strftime("%y"))
        self.mes = int(date.today().strftime("%m"))
        self.hoje = int(date.today().strftime("%d"))
    
    def log(self, msg:str):
      print(f"{'=' * 100}\n{Fore.YELLOW}{msg}{Style.RESET_ALL}\n{'=' * 100}")

    def wait_elements(self, element: str):
      try:
        maxLoop = 0
        listElement = self.inBrowser.find_elements(self.selectItem.XPATH, element)
        while len(listElement) < 1 and maxLoop < 600:
            time.sleep(1)
            maxLoop += 1
        time.sleep(1)
        return self.inBrowser.find_element(self.selectItem.XPATH, element)
      except:
          if len(listElement) < 1:
            self.log("Tempo esgotado, não houve resposta do servidor")
            return
          pass

    def wait_load_data(self):
        load = self.inBrowser.find_elements(
            self.selectItem.XPATH, '//*[@id="M0:46:::0:0-groupheader"]'
        )
        while len(load) > 0:
            load = self.inBrowser.find_elements(
                self.selectItem.XPATH, '//*[@id="M0:46:::0:0-groupheader"]'
            )
            time.sleep(3)
    def killBrowser(self):
        self.log('Fechando navegador')
        try:
            self.inBrowser.quit()
        except:
            self.inBrowser.close()
