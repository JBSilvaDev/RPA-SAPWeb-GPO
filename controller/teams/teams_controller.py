import pymsteams
import sys
from controller.variaveis import *
from data.controller import DbFilter
from models.msg_model import MsgModel

df = DbFilter()


class TeamsController:
    def __init__(self):
        self.team = TEAMS_LINKS["oficial"]
        self.team_model = MsgModel()
        self.connect = pymsteams.connectorcard(self.team, verify=False)
        self.create_card = pymsteams.cardsection()
        self.dic = self.team_model.msg_final

    def send_teams(self):
        self.connect.text(" ")
        self.create_card.activityTitle("Logística Celulose Mucuri")
        self.create_card.activityImage(self.team_model.logo)
        self.create_card.activityText(self.team_model.activityText)
        self.create_card.text(self.team_model.title_msg)
        for key in self.dic:
            self.create_card.addFact(str(key), str(self.dic[key]))
        self.connect.addSection(self.create_card)
        self.connect.send()
