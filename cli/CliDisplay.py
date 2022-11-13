import os

class CliDisplay():
    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def update_score(self, voter):
        self._clear_screen()
        print('A', voter.voteA)
        print('B', voter.voteB)

    def send_vote(self, voteA, voteB):
        self._clear_screen()
        print('Sending: ', voteA, voteB)

    def show_total(self, voteA, voteB):
        self._clear_screen()
        print('Total: ', voteA, voteB)

    def show_info(self, deviceName, pollName):
        self._clear_screen()
        print('Device:', deviceName)
        print('Poll:', pollName)

