from CharacterDisplay import CharacterDisplay
from Display import Display
from VoterCounter import VoterCounter

class IoTDisplay(Display):
    display = None

    def __init__(self, config):
        self.display = CharacterDisplay(config)

    def update_score(self, voter: VoterCounter):
        self.display.send_message(str(voter.voteA), str(voter.voteB))

    def send_vote(self, voteA, voteB):
        self.display.send_message("Sending votes", "A: [" + str(voteA) + "] B: [" + str(voteB) + "]")

    def show_total(self, voteA, voteB):
        self.display.send_message("Total votes", "A: [" + str(voteA) + "] B: [" + str(voteB) + "]")

    def show_info(self, deviceName, pollName):
        self.display.send_message(deviceName, pollName)

