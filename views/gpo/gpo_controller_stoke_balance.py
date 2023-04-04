import time
from controller.gpo.gpo_controller import GpoController


class GpoBalance(GpoController):

    def __init__(self):
        super().__init__()

    def gpo_start(self):
        self.wait_load_data()
        self.gpo_download_csv()


    def wait_load_data(self):
        time.sleep(5)
        self.inBrowser.get(self.gpo_model.links['relatorio'])
        time.sleep(5)
    
    def gpo_download_csv(self):
        print('--'*100)
        self.wait_elements('//*[@id="StiViewer_JsViewerMainPanel"]/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div/table/tbody/tr/td[3]/img').click()
        self.wait_elements('/html/body/form/div/div/div/div[14]/div/div[11]/table/tbody/tr/td[2]').click()
        self.wait_elements('/html/body/form/div/div/div/div[18]/div[4]/table/tbody/tr/td[1]/div/table/tbody/tr/td').click()
        time.sleep(15)
        self.inBrowser.quit()
