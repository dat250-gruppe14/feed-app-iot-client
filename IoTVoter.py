from voter import Voter
from display import IoTDisplay

class IoTVoter(Voter):
    def __init__(self, config):
        self.config = config
        self.display = IoTDisplay(config)

    def add_voteA(self, channel):
        super().add_voteA()
        self.update_display()

    def add_voteB(self, channel):
        super().add_voteB()
        self.update_display()

    def update_display(self):
        self.display.send_message(str(self.voteA), str(self.voteB))

    def send_vote(self, channel):
        v1, v2 = super().send_vote()
        self.display.send_message(
                'Sending votes:', 
                'A:[' + str(v1) + '] B: [' + str(v2) + ']'
                )


