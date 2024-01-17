from enum import verify
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By as selectItem
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import date, datetime
from selenium.webdriver.common.alert import Alert
import time
import colorama
from colorama import Fore
from colorama import Style
from pathlib import Path
import os
# import urllib3


# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

path_locate = Path(r'C:\Users\julianobs\Dev\Report-Logistc')
# service = Service()
# service = Service(version='117.0.5938.1100-beta')


def enable_download(driver):
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": os.path.join(path_locate,"Arquivos")},
    }
    driver.execute("send_command", params)


edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--headless")
edge_options.add_argument("--no-sandbox")
edge_options.add_argument("--ignore-certificate-errors")
edge_options.add_argument("--disable-Dev-shm-usage")
# edge_options.add_argument(r'user-data-dir=C:\Users\julianobs\AppData\Local\Google\Chrome\User Data\Perfil Selenium')
prefs = {
    "download.default_directory": os.path.join(path_locate,"Arquivos"),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}

edge_options.experimental_options["prefs"] = prefs
inBrowser = webdriver.Edge(
    # service=service,
    options=edge_options,
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

    def log(self, msg: str):
        edge_options.add_argument("--headless")
        # format_text  = '\033[33;40;1;4m'
        # reset_format  = '\033[0m'
        # print(f"{'=' * 100}\n{format_text}{msg}\n{reset_format}{'=' * 100}")
        # print(f"{'=' * 100}\n{msg}\n{'=' * 100}")
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
        self.log("Fechando navegador")
        try:
            self.in_browser.close()
            self.in_browser.service.stop()
        except:
            self.inBrowser.quit()
