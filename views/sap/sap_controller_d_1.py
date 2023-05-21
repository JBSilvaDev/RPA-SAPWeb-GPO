from controller.sap.sap_controller import SapController
import time
import calendar


class SapD_1(SapController):
    def __init__(self):
        super().__init__()
        self.index_transaction = 0

    def sap_start(self):
        self.surf_page()
        self.sap_menu_ambiente()
        self.sap_page_action()
        self.wait_load_data()
        self.sap_download_csv()

    def surf_page(self):
        self.log("Acessando SQ01 para faturado D-1")
        iD_transactions = self.sap_model.transacoes
        self.wait_elements('//*[@id="ToolbarOkCode"]').send_keys(
            iD_transactions[self.index_transaction]
        )
        self.wait_elements('//*[@id="ToolbarOkCode"]').send_keys(self.key.ENTER)

    def sap_menu_ambiente(self):
        self.log("Configurando ambiente")
        self.wait_elements('//*[@id="cua2sapmenu_btn"]').click()
        ambiente = self.wait_elements(
            "/html/body/table/tbody/tr/td/div/div/div/div[2]/span[1]/div/div[2]/table/tbody/tr[6]/td[3]"
        )
        hover = self.action_chains.move_to_element(ambiente)
        hover.perform()
        time.sleep(2)
        area_de_trabalho = self.wait_elements(
            "/html/body/table/tbody/tr/td/div/div/div/div[2]/span[20]/div/div[2]/table/tbody/tr[1]/td[3]/span"
        )
        area_de_trabalho.click()
        time.sleep(2)
        self.wait_elements('//*[@id="M1:46:::0:0-txt"]').click()

        self.wait_elements('//*[@id="M1:37::btn[2]"]').click()
        self.log("Acessando SD114")
        self.wait_elements('//*[@id="M0:46:::2:21"]').send_keys("SD114")

        self.wait_elements('//*[@id="M0:46:::2:21"]').send_keys(self.key.F8)

    def sap_page_action(self):
        self.log("Acessando dados faturamento")
        if self.hoje == 1:
            self.hoje = int(calendar.monthrange(self.ano, self.mes - 1)[1])
            self.mes = self.mes - 1
        else:
            self.hoje = self.hoje - 1
        time.sleep(10)
        self.wait_elements('//*[@id="M0:46:::1:34"]').send_keys("MUCU")
        self.wait_elements('//*[@id="M0:46:::2:34"]').send_keys("02")
        self.wait_elements('//*[@id="M0:46:::4:34"]').send_keys("CE")
        self.wait_elements('//*[@id="M0:46:::4:59"]').send_keys("CE")
        self.wait_elements('//*[@id="M0:46:::5:34"]').send_keys(
            f"{self.hoje}.{self.mes}.20{self.ano}"
        )
        self.wait_elements('//*[@id="M0:46:::5:59"]').send_keys(
            f"{self.hoje}.{self.mes}.20{self.ano}"
        )
        self.wait_elements('//*[@id="M0:46:::15:34"]').send_keys("/JBESCOAMENT")
        self.wait_elements('//*[@id="M0:46:::15:4"]').click()
        time.sleep(6)
        self.wait_elements('//*[@id="M0:37::btn[8]"]').click()

    def sap_download_csv(self):
        self.log("Inciando download faturado d-1")
        self.wait_elements('//*[@id="cua2sapmenu_btn"]').click()
        self.wait_elements(
            "/html/body/table/tbody/tr/td/div/div/div[1]/div[2]/span[1]/div/div[2]/table/tbody/tr[1]/td[3]"
        ).click()
        self.wait_elements(
            "/html/body/table/tbody/tr/td/div/div/div[1]/div[2]/span[5]/div/div[2]/table/tbody/tr[4]/td[3]"
        ).click()
        self.wait_elements(
            "/html/body/table/tbody/tr/td/div/div/div[1]/div[2]/span[3]/div/div[2]/table/tbody/tr[3]/td[3]/span"
        ).click()
        time.sleep(5)
        self.wait_elements('//*[@id="M1:46:2:1::1:0-txt"]').click()
        self.wait_elements('//*[@id="M1:37::btn[0]"]').click()
        time.sleep(10)
        self.wait_elements('//*[@id="M1:46:::1:12"]').send_keys(r"BDFaturamentoD-1.CSV")
        self.wait_elements('//*[@id="M1:37::btn[11]"]').click()
        self.log("Finalizando download faturado d-1")
        time.sleep(10)
