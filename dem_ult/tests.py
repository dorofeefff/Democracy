import coverage.results
from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number > 1:
            if self.round_number % 2 == 0:
                yield Voting, {"vote": 1}
            elif self.round_number % 2 != 0:
                yield Voting, {"vote": 0}
            yield VotingResults
            if (self.round_number % 2 == 0) & (not self.group.overridden):
                assert self.group.final_group_choice == 1
            elif (self.round_number % 2 != 0) & (not self.group.overridden):
                assert self.group.final_group_choice == 0
        if self.player.role == C.SENDER_ROLE:
            yield DictatorSend, {"send": 300}
            if self.player.round_number in {C.NUM_ROUNDS, 1}:
                yield DictatorResults
        elif self.player.role == C.GUESSER_ROLE:
            yield DictatorGuess, {"guess": 295}
            if self.player.round_number in {C.NUM_ROUNDS, 1}:
                yield DictatorResults
        elif self.player.role == C.RECEIVER_ROLE:
            if self.player.round_number in {C.NUM_ROUNDS, 1}:
                yield DictatorResults
        if self.round_number == 1:
            yield Submission(WaitBetweenParts, check_html=False)
        if self.round_number == 1:
            yield Comprehension1
            yield Comprehension2
            yield Comprehension3
            yield Comprehension4
        if self.round_number == C.NUM_ROUNDS:
            yield Feedback, {"feedback": "test"}
            payoff_dictionary = {C.SENDER_ROLE: 700,
                                 C.GUESSER_ROLE: 500,
                                 C.RECEIVER_ROLE: 300}

            payoff_logic = sum(
                [1 * payoff_dictionary[self.player.in_round(j+1).role] for j in range(C.NUM_ROUNDS)])
            payoff_actual = sum(
                [p.payoff for p in self.player.in_all_rounds()])

            assert payoff_actual == payoff_logic
