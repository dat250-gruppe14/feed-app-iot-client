class CliController:
    def __init__(self, voter):
        self.voter =voter

    def run(self):
        inp = ''
        while inp != 'q':
            inp = input()
            if inp == 'a':
                self.voter.add_voteA()
            if inp == 'b':
                self.voter.add_voteB()
            if inp == 's':
                self.voter.send_vote()
            if inp == 'd':
                self.voter.get_total()
