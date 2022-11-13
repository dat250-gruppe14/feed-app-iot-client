class VoterCounter:
    voteA = 0
    voteB = 0
    
    def add_voteA(self):
        self.voteA += 1

    def add_voteB(self):
        self.voteB += 1

    def send_vote(self):
        voteA, voteB = self.voteA, self.voteB
        self.voteA = 0
        self.voteB = 0
        return voteA, voteB
