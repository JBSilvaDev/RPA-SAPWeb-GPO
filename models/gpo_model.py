from controller.user_key.key_controller import ControllerLogin

controller = ControllerLogin()
controller.find_user_gpo()


class GpoModel:
    def __init__(self):
        self.links = {
            "home_login": "https://web.portocel.com.br/gpo/",
            "relatorio": "https://web.portocel.com.br/gpo/relatorio",
        }
        self.usuario = controller.username
        self.senha = controller.password
        self.estoque_armazem = ""
