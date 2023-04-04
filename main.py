from views.gpo.gpo_controller_stoke_balance import GpoBalance
from views.sap.sap_controller_d_1 import SapD_1
from views.sap.sap_controller_mouth import SapMonth
from views.sap.sap_controller_production_d_1 import SapProduction
from views.sap.sap_stoke_balance import SapBalace
from controller.whats.whats_controller import WhatsController
from data.controller import DbFilter
from pathlib import Path
from controller.teams.teams_controller import TeamsController
import os
from pathlib import Path
from controller.user_key.key_controller import ControllerLogin
from datetime import datetime


  # # Remove CSVs antigos
try:
  path = Path('./').absolute()
  pasta = os.listdir(f'{path}\Arquivos')
  for i in pasta:
      os.unlink(f'{path}\Arquivos\{i}')
except:
  pass



# Baixando dados
SapD_1().sap_start()
SapBalace().sap_start()
SapProduction().sap_start()
SapMonth().sap_start()
GpoBalance().gpo_start()

# Tratando CSVs
db = DbFilter()
db.sap_balance()
db.gpo_balance()
db.sap_d_1()
db.sap_month()
db.sap_product()

# Enviando msg
teams = TeamsController()
teams.send_teams()
zap = WhatsController()
zap.send_messeger()

# Salvando ultimo registro
data = f'{datetime.today().date().strftime("%d-%m-%Y")}'
hora = f'{datetime.today().time().strftime("%H:%M")}'
firebase = ControllerLogin()
firebase.last_run({data:hora})



