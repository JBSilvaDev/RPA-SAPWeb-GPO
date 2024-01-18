import requests
import json

from controller.variaveis import *


class ControllerLogin:
    def __init__(self):
        self.link_firebase = LINK_FIREBASE
        self.username = ""
        self.password = ""
        self.number = ""

    def _find_all(self, firebase_folder: str):
        request = requests.get(
            f"{self.link_firebase}/{firebase_folder}/.json", verify=False
        )
        user = request.json()
        return user

    def find_user_sap(self):
        user = self._find_all("SAP_Login")
        self.username = user["login"]
        self.password = user["password"]
        return [self.username, self.password]

    def find_user_gpo(self):
        user = self._find_all("GPO_Login")
        self.username = user["login"]
        self.password = user["password"]
        return [self.username, self.password]

    def find_number_whatsApp(self):
        # ID para msgs
        key = self._find_all("Msg")
        # Envio de msg para
        self.number = key["Daiane"]
        return self.number

    def last_run(self, map: dict):
        map = json.dumps(map)
        request = requests.post(
            f"{self.link_firebase}/Lasts_runs/.json", data=map, verify=False
        )
