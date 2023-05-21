from pathlib import Path
import os
from controller.teams.teams_controller import TeamsController
from controller.user_key.key_controller import ControllerLogin
from controller.whats.whats_controller import WhatsController
from data.controller import DbFilter
from views.gpo.gpo_controller_stoke_balance import GpoBalance
from views.sap.sap_controller_d_1 import SapD_1
from views.sap.sap_controller_mouth import SapMonth
from views.sap.sap_controller_production_d_1 import SapProduction
from views.sap.sap_stoke_balance import SapBalance
from datetime import datetime
import colorama
from colorama import Fore, Style
import sys


colorama.init()


# Função para exibir dados no console
def log(msg: str):
    print(f"{'=' * 100}\n{Fore.YELLOW}{msg}{Style.RESET_ALL}\n{'=' * 100}")


def main():
    # Remove CSVs antigos
    path = Path("C:/Users/julianobs/Desktop/Report-Logistc")
    print(f"{Fore.RED} {path}{Style.RESET_ALL}")
    pasta = os.listdir(f"{path}/Arquivos")
    try:
        print(Fore.RED, pasta, Style.RESET_ALL)
        for i in pasta:
            os.unlink(f"{path}/Arquivos/{i}")
            print(f"{Fore.RED}{i} -> Removido{Style.RESET_ALL}")
    except:
        pass

    # Baixando dados
    SapD_1().sap_start()
    SapBalance().sap_start()
    SapProduction().sap_start()
    SapMonth().sap_start()
    GpoBalance().gpo_start()

    # Tratando CSVs
    db = DbFilter()
    db.data_processing()

    # Enviando msg
    teams = TeamsController()
    log('Enviando dados no teams')
    teams.send_teams()
    zap = WhatsController()
    log('Enviando dados no WhatsApp')
    zap.send_messenger()

    # Salvando ultimo registro
    log("Salvando dados no firebase")
    data = datetime.today().strftime("%d-%m-%Y")
    hora = datetime.now().strftime("%H:%M")
    firebase = ControllerLogin()
    firebase.last_run({data: hora})
    sys.exit(0)


if __name__ == "__main__":
    main()
