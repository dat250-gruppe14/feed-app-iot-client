from FeedAppClient import FeedAppClient
from FeedAppVoter import FeedAppVoter
from IoTDisplay import IoTDisplay
from IoTController import IoTController
from VoterCounter import VoterCounter
from board_config import board_config
import json

if __name__ == '__main__':
    client = None
    with open('config.json') as j:
        client = FeedAppClient(json.load(j))

    display = IoTDisplay(board_config)
    voterCounter = VoterCounter()
    voter = FeedAppVoter(voterCounter, client, display)

    controller = IoTController(voter)
    controller.run()
