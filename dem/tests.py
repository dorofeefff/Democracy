from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        if self.player.round_number == 1:
            if self.player.type == "Sender":
                yield DictatorOffer, {"kept": 7}
                yield DictatorBeliefs, {"beliefs": 8}
                yield DictatorResults
            else:
                yield DictatorBeliefs, {"beliefs": 8}
                yield DictatorResults
        elif self.player.round_number < C.NUM_ROUNDS:
            if self.player.type == "Sender":
                yield Voting, {"vote": 1}
                yield VotingResults
                yield DictatorOffer, {"kept": 7}
                yield DictatorBeliefs, {"beliefs": 8}
                yield DictatorResults
            else:
                yield Voting, {"vote": 0}
                yield VotingResults
                yield DictatorBeliefs, {"beliefs": 8}
                yield DictatorResults
        else:
            if self.player.type == "Sender":
                yield Voting, {"vote": 1}
                yield VotingResults
                yield DictatorOffer, {"kept": 7}
                yield DictatorBeliefs, {"beliefs": 8}
                yield DictatorResults
                yield Feedback, {"feedback": "I'm dictating"}
            else:
                yield Voting, {"vote": 0}
                yield VotingResults
                yield DictatorBeliefs, {"beliefs": 8}
                yield DictatorResults
                yield Feedback, {"feedback": "I'm receiving"}


