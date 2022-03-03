import coverage.results
from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    cases = ['unanimity', 'two_votes', 'unanimity_guesser_wrong']
    assert C.NUM_ROUNDS >= 10, "Set Constant NUM_ROUNDS to least 10 for testing!"

    def play_round(self):
        assert len(self.subsession.get_players()) >= 6, "Set num_demo_participants in settings to at least 6!"
        if self.round_number > 1:
            if 'unanimity' in self.case:
                yield Voting, {"vote": 1 * (self.round_number % 2 == 0)}
            elif self.case == 'two_votes':
                yield Voting, {"vote": 1 * (self.round_number % 2 == 0) *
                                       (self.player.id_in_group % 2 != 0) +
                                       1 * (self.round_number % 2 != 0) *
                                       (self.player.id_in_group % 2 == 0)
                               }
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
            if self.case == "unanimity_guesser_wrong":
                yield DictatorGuess, {"guess": 289}
            else:
                yield DictatorGuess, {"guess": 291}
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
            if "guesser_wrong" in self.case:
                payoff_dictionary = {C.SENDER_ROLE: 700,
                                     C.GUESSER_ROLE: 0,
                                     C.RECEIVER_ROLE: 300}
            else:
                payoff_dictionary = {C.SENDER_ROLE: 700,
                                     C.GUESSER_ROLE: C.GUESSER_BONUS,
                                     C.RECEIVER_ROLE: 300}
            payoff_logic = sum(
                [1 * payoff_dictionary[self.player.in_round(j+1).role] for j in range(C.NUM_ROUNDS)])
            payoff_actual = sum(
                [p.payoff for p in self.player.in_all_rounds()])
            assert payoff_actual == payoff_logic, "Payoffs are wrong!"
            role_variation = set([1 * (self.player.in_round(j+1).role == C.SENDER_ROLE)
                                  + 2 * (self.player.in_round(j+1).role == C.GUESSER_ROLE)
                                  for j in range(C.NUM_ROUNDS)])
            assert len(role_variation) != 1, "Roles are not changing!"
