from controller.user_key.key_controller import ControllerLogin

controller = ControllerLogin()
controller.find_user_sap()


class SapModel:
    def __init__(self):
        self.home_login = "https://ecphanacls.suzano.com.br:8101/sap/bc/gui/sap/its/webgui?sap-client=500&sap-language=PT"
        self.usuario = controller.username
        self.senha = controller.password
        self.transacoes = ["/nSQ01", "/nMB51", "/nLX02"]
        self.layouts = ["/JBESCOAMENT"]
