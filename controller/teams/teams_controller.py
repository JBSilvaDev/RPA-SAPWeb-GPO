import pymsteams
import sys
from data.controller import DbFilter
from models.msg_model import MsgModel

# Link para canal teste:
# https://suzano.webhook.office.com/webhookb2/3b359661-e945-4103-8cc8-2e572244d2c9@a7109315-9727-4adf-97ad-4849bb63edcb/IncomingWebhook/b3f8aa0c8fae43d49439d97c9de265a2/84b16ee0-4575-45d0-9876-b397b0f8c957

# Link canal oficial
# https://suzano.webhook.office.com/webhookb2/ca9b57cd-1eb0-403a-ae6a-b38719e81c4b@a7109315-9727-4adf-97ad-4849bb63edcb/IncomingWebhook/24112f269e644203bd4b6e205ed45179/84b16ee0-4575-45d0-9876-b397b0f8c957

teams_links = {
    "testes": "https://suzano.webhook.office.com/webhookb2/3b359661-e945-4103-8cc8-2e572244d2c9@a7109315-9727-4adf-97ad-4849bb63edcb/IncomingWebhook/b3f8aa0c8fae43d49439d97c9de265a2/84b16ee0-4575-45d0-9876-b397b0f8c957",
    "oficial": "https://suzano.webhook.office.com/webhookb2/ca9b57cd-1eb0-403a-ae6a-b38719e81c4b@a7109315-9727-4adf-97ad-4849bb63edcb/IncomingWebhook/24112f269e644203bd4b6e205ed45179/84b16ee0-4575-45d0-9876-b397b0f8c957",
}
df = DbFilter()


class TeamsController:
    def __init__(self):
        self.team = teams_links["oficial"]
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
