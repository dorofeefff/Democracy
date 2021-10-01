from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'democracy_mechanism'
    players_per_group = 2
    num_rounds = 2
    # Initial amount allocated to the dictator
    endowment = cu(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Treatment
    treatment = models.StringField(
        initial='"hallo"'
    )
    # Voting stage
    group_choice = models.BooleanField()
    overridden = models.BooleanField()
    final_choice = models.BooleanField()
    # Dictator stage
    kept = models.CurrencyField()


class Player(BasePlayer):
    vote = models.BooleanField(
        label="What do you want?",
        choices=[[True, "Add fair distribution"], [False, "Add unfair distribution"]]
    )


# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = group.kept
    p2.payoff = Constants.endowment - group.kept


# PAGES
class Voting(Page):
    form_model = "player"
    form_fields = ["vote"]

    @staticmethod
    def is_displayed(player):
        return player.round_number > 1


class ResultsWaitVoting(WaitPage):
    @staticmethod
    def is_displayed(player):
        return player.round_number > 1

    @staticmethod
    def after_all_players_arrive(group: Group):
        import random

        # Determine majority vote
        votes_for_a = 0
        for p in group.get_players():
            votes_for_a += int(p.vote)
        if votes_for_a * 2 > Constants.players_per_group:
            group.group_choice = True
        elif votes_for_a * 2 < Constants.players_per_group:
            group.group_choice = False
        else:
            group.group_choice = random.choice([True, False])

        # Random overriding
        group.overridden = random.choice([True, False])

        # Determine final choice
        if group.overridden:
            group.final_choice = random.choice([True, False])
        else:
            group.final_choice = group.group_choice


class VotingResults(Page):
    form_model = "group"

    @staticmethod
    def is_displayed(player):
        return player.round_number > 1


class DictatorOffer(Page):
    form_model = 'group'
    form_fields = ['kept']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group % 2 == 1


class ResultsWaitDictator(WaitPage):
    after_all_players_arrive = set_payoffs


class DictatorResults(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(offer=Constants.endowment - group.kept)


page_sequence = [Voting, ResultsWaitVoting, VotingResults, DictatorOffer, ResultsWaitDictator, DictatorResults]
