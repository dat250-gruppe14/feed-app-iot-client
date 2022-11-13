from board_config import board_config
from button import IoTButtons

class IoTController:
    def __init__(self, voter):
        self.buttons = IoTButtons([
	     (board_config['button1'], voter.add_voteA),
	     (board_config['button2'], voter.add_voteB),
	     (board_config['button3'], voter.send_vote),
        ])

    def run(self):
        message = input('Press enter to quit')
        return message
