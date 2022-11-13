from VoterCounter import VoterCounter
from Display import Display
from FeedAppClient import FeedAppClient

class FeedAppVoter:
    voter = None
    client = None
    display = None

    def __init__(self, voter, client, display):
        self.voter = voter
        self.client = client
        self.display = display
        device = self.client.getDevice()
        self.display.show_info(device['name'], device['connectedPoll']['question'])

    def add_voteA(self, channel=None):
        self.voter.add_voteA()
        self.display.update_score(self.voter)
        
    def add_voteB(self, channel=None):
        self.voter.add_voteB()
        self.display.update_score(self.voter)

    def send_vote(self, channel=None):
        voteA, voteB = self.voter.send_vote()
        if voteA == 0 and voteB == 0:
            self.get_total()
        else:
            self.display.send_vote(voteA, voteB)
            self.client.sendVotes(voteA, voteB)
            return voteA, voteB

    def get_total(self, channel=None):
        device = self.client.getDevice()
        self.display.show_total(
            device['connectedPoll']['counts']['optionOneCount'],
            device['connectedPoll']['counts']['optionTwoCount'])


