import requests
import json


class ControllerLogin:
    def __init__(self):
        self.link_firebase = "https://projeto-firebase.firebaseio.com/"
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
        key = self._find_all("Msg")
        self.number = key["Ricardo"]
        return self.number

    def last_run(self, map: dict):
        map = json.dumps(map)
        print(map)
        request = requests.post(
            f"{self.link_firebase}/Lasts_runs/.json", data=map, verify=False
        )
        print(request)
