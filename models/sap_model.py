from controller.user_key.key_controller import ControllerLogin

controller = ControllerLogin()
controller.find_user_sap()


class SapModel:
    def __init__(self):
        self.home_login = "https://sap.com/seusapaqui"
        self.usuario = controller.username
        self.senha = controller.password
        self.transacoes = ["/nSQ01", "/nMB51", "/nLX02"]
        self.layouts = ["/JBESCOAMENT"]
