import time
from controller.controller import Controller
from models.sap_model import SapModel

class SapController(Controller):

    def __init__(self):
        super().__init__()
        self.sap_model = SapModel()
        self.open_browser()
        
    
    def open_browser(self):
        self.inBrowser.get(self.sap_model.home_login)
        self.logon_sap()
        self.iframe_access()
    
    
    def logon_sap(self):
        self.wait_elements('//*[@id="sap-user"]').send_keys(self.sap_model.usuario)
        self.wait_elements('//*[@id="sap-password"]').send_keys(self.sap_model.senha)
        self.wait_elements('//*[@id="LOGON_BUTTON"]').click()
            
    def iframe_access(self):
        self.inBrowser.switch_to.frame(self.wait_elements('//*[@id="ITSFRAME1"]'))
    





