from controller.user_key.key_controller import ControllerLogin

controller = ControllerLogin()
controller.find_user_gpo()

class GpoModel:
  def __init__(self):
    self.links = {'home_login':'https://site.porto.gpo', 
                  'relatorio':"https://site.porto.gpo/link_direto_download_csv"
                  }
    self.usuario = controller.username
    self.senha = controller.password
    self.estoque_armazem = ''
