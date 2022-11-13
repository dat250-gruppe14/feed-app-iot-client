from FeedAppClient import FeedAppClient
from FeedAppVoter import FeedAppVoter
from CliDisplay import CliDisplay
from CliController import CliController
from VoterCounter import VoterCounter
import json

if __name__ == '__main__':
    client = None
    with open('config.json') as j:
        client = FeedAppClient(json.load(j))

    display = CliDisplay()
    voterCounter = VoterCounter()
    voter = FeedAppVoter(voterCounter, client, display)

    controller = CliController(voter)
    controller.run()
