from controller.sap.sap_controller import SapController
import time
import calendar
from datetime import date


class SapBalace(SapController):
    def __init__(self):
        super().__init__()
        self.ano = int(date.today().strftime("%y"))
        self.mes = int(date.today().strftime("%m"))
        self.index_transaction = 2
        self.end_month = int(calendar.monthrange(self.ano, self.mes)[1])

    def open_browser(self):
        # Pagina ja aberta, caso sera start solo, eliminar esta função
        pass

    def logon_sap(self):
        # Pagina ja aberta, caso sera start solo, eliminar esta função
        pass

    def iframe_access(self):
        # Pagina ja aberta, caso sera start solo, eliminar esta função
        pass

    def sap_start(self):
        self.surf_page()
        self.sap_page_action()
        self.wait_load_data()
        self.sap_download_csv()

    def surf_page(self):
        iD_transactions = self.sap_model.transacoes
        self.wait_elements('//*[@id="ToolbarOkCode"]').send_keys(
            iD_transactions[self.index_transaction]
        )
        self.wait_elements('//*[@id="ToolbarOkCode"]').send_keys(self.key.ENTER)

    def sap_menu_ambiente(self):
        # Desnecessário para esta transação
        pass

    def sap_page_action(self):
        time.sleep(10)
        # aguardarElemento('//*[@id="M0:46:::0:34"]').send_keys('004')
        # aguardarElemento('//*[@id="M0:46:::1:34"]').send_keys('CES')
        # aguardarElemento('//*[@id="M0:46:::14:34"]').send_keys('/julianobs')
        # aguardarElemento('//*[@id="M0:46:::14:34"]').send_keys(Keys.F8)
        self.wait_elements('//*[@id="M0:46:::0:34"]').send_keys("004")
        self.wait_elements('//*[@id="M0:46:::1:34"]').send_keys("CES")
        self.wait_elements('//*[@id="M0:46:::14:34"]').send_keys("/julianobs")
        self.wait_elements('//*[@id="M0:37::btn[8]"]').click()

    def sap_download_csv(self):
        time.sleep(20)
        self.wait_elements('//*[@id="cua2sapmenu_btn"]').send_keys(self.key.F9)
        time.sleep(5)
        self.wait_elements('//*[@id="M1:46:2:1::1:0-txt"]').click()
        self.wait_elements('//*[@id="M1:37::btn[0]"]').click()
        time.sleep(5)
        self.wait_elements('//*[@id="M1:46:::1:12"]').send_keys(r"BDEstoque.CSV")
        self.wait_elements('//*[@id="M1:37::btn[11]"]').click()
        time.sleep(10)
