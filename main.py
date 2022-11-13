import json
import sys

from VoterCounter import VoterCounter
from FeedAppClient import FeedAppClient
from FeedAppVoter import FeedAppVoter

def isIoT():
    return len(sys.argv) > 1 and sys.argv[1] == 'iot'

def get_display():
    if isIoT():
        from iot.IoTDisplay import IoTDisplay
        return IoTDisplay()
    from cli.CliDisplay import CliDisplay
    return CliDisplay()

def get_controller(voter):
    if isIoT():
        from iot.IoTController import IoTController
        return IoTController(voter)
    from cli.CliController import CliController
    return CliController(voter)



if __name__ == '__main__':
    client = None
    with open('config.json') as j:
        client = FeedAppClient(json.load(j))

    voterCounter = VoterCounter()

    display = get_display()

    voter = FeedAppVoter(voterCounter, client, display)

    controller = get_controller(voter)
    controller.run()

