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
    endowment = cu(10)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Treatment
    treatment = models.StringField(
        initial='"default"'
    )
    # Voting stage
    group_vote = models.BooleanField()
    overridden = models.BooleanField()
    final_group_choice = models.BooleanField()
    # Dictator stage
    kept = models.CurrencyField()


class Player(BasePlayer):
    vote = models.BooleanField(
        label="What do you want?",
        choices=[[True, "Add fair distribution"], [False, "Add selfish distribution"]]
    )


# FUNCTIONS
def set_payoffs(group: Group):
    # Sets payoffs for dictator (p1) and receiver (p2)
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
            group.group_vote = True
        elif votes_for_a * 2 < Constants.players_per_group:
            group.group_vote = False
        else:
            group.group_vote = random.choice([True, False])

        # Random overriding
        group.overridden = random.choice([True, False])

        # Determine final choice
        if group.overridden:
            group.final_group_choice = random.choice([True, False])
        else:
            group.final_group_choice = group.group_vote

        # Change group treatment variable
        if group.final_group_choice:
            group.treatment = '"selfish"'
        else:
            group.treatment = '"fair"'


class VotingResults(Page):
    form_model = "group"

    # First round of dictator game happens without voting
    @staticmethod
    def is_displayed(player):
        return player.round_number > 1

    @staticmethod
    def vars_for_template(player):
        translate = {True: "Fair distribution", False: "Selfish distribution"}
        return dict(
            group_vote=translate[player.group.group_vote],
            overridden=player.group.overridden,
            final=translate[player.group.final_group_choice]
        )



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
    def vars_for_template(player):
        group = player.group
        return dict(offer=Constants.endowment - group.kept)


page_sequence = [Voting, ResultsWaitVoting, VotingResults, DictatorOffer, ResultsWaitDictator, DictatorResults]
