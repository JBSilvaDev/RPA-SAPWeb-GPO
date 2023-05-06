import time
from models.gpo_model import GpoModel
from controller.controller import Controller


class GpoController(Controller):
    def __init__(self):
        super().__init__()
        self.gpo_model = GpoModel()
        self.open_browser()

    def open_browser(self):
        self.inBrowser.get(self.gpo_model.links["home_login"])
        self.logon_gpo()

    def logon_gpo(self):
        time.sleep(5)
        try:
            from selenium.webdriver.common.alert import Alert

            alert = Alert(self.inBrowser)
            alert.accept()
        except:
            pass
        self.wait_elements(
            "/html/body/form/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td[2]/input"
        ).send_keys(self.gpo_model.usuario)
        self.wait_elements(
            "/html/body/form/center/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/input"
        ).send_keys(self.gpo_model.senha)
        self.wait_elements('//*[@id="tbrImg"]').click()
        time.sleep(5)
