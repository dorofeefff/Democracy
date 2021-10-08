from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'democracy_mechanism'
    players_per_group = 4
    num_rounds = 2
    # Initial amount allocated to the dictator
    endowment = cu(10)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # mode
    mode = models.StringField(
        initial='"default"'
    )
    # Voting stage
    group_vote = models.IntegerField()
    overridden = models.BooleanField()
    final_group_choice = models.IntegerField()


class Player(BasePlayer):
    # Voting stage
    vote = models.IntegerField(
        label="What do you want?",
        choices=[[0, "Add fair distribution"], [1, "Add selfish distribution"]]
    )
    # Dictator stage
    kept = models.CurrencyField(
        initial=0
    )


# FUNCTIONS
def set_payoffs(group: Group):
    # Sets payoffs for dictators (odd ids) and receiver (even ids)
    for i in range(1, Constants.players_per_group, 2):
        dictator = group.get_player_by_id(i)
        receiver = group.get_player_by_id(i+1)
        dictator.payoff = dictator.kept
        receiver.payoff = Constants.endowment - dictator.kept


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
        sum_vote = 0
        for p in group.get_players():
            sum_vote += p.vote
        if sum_vote * 2 < Constants.players_per_group:
            group.group_vote = 0  # majority for 0
        elif sum_vote * 2 > Constants.players_per_group:
            group.group_vote = 1  # majority for 1
        else:
            group.group_vote = 2  # group tied

        # Random overriding
        group.overridden = random.choice([True, False])

        # Determine final choice
        if group.overridden or group.group_vote == 2:
            group.final_group_choice = random.choice([0, 1])
        else:
            group.final_group_choice = group.group_vote

        # Change group mode variable
        if group.final_group_choice == 0:
            group.mode = '"fair"'
        else:
            group.mode = '"selfish"'


class VotingResults(Page):
    form_model = "group"

    # First round of dictator game happens without voting
    @staticmethod
    def is_displayed(player):
        return player.round_number > 1

    @staticmethod
    def vars_for_template(player):
        translate = {0: "Fair distribution", 1: "Selfish distribution", 2: "Tie"}
        return dict(
            group_vote=translate[player.group.group_vote],
            overridden=player.group.overridden,
            final=translate[player.group.final_group_choice]
        )


class DictatorOffer(Page):
    form_model = 'player'
    form_fields = ['kept']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group % 2 == 1


class ResultsWaitDictator(WaitPage):
    after_all_players_arrive = set_payoffs


class DictatorResults(Page):
    pass
    @staticmethod
    def vars_for_template(player):
        x = player.id_in_group
        dictator = player.group.get_player_by_id(x - ((x+1) % 2))
        return dict(kept=dictator.kept, offer=Constants.endowment - dictator.kept)


page_sequence = [Voting, ResultsWaitVoting, VotingResults, DictatorOffer, ResultsWaitDictator, DictatorResults]
