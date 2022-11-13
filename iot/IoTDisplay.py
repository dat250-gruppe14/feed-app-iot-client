from iot.CharacterDisplay import CharacterDisplay
from iot.board_config import board_config

class IoTDisplay():
    def __init__(self):
        self.display = CharacterDisplay(board_config)

    def update_score(self, voter):
        self.display.send_message(str(voter.voteA), str(voter.voteB))

    def send_vote(self, voteA, voteB):
        self.display.send_message("Sending votes", "A: [" + str(voteA) + "] B: [" + str(voteB) + "]")

    def show_total(self, voteA, voteB):
        self.display.send_message("Total votes", "A: [" + str(voteA) + "] B: [" + str(voteB) + "]")

    def show_info(self, deviceName, pollName):
        self.display.send_message(deviceName, pollName)

