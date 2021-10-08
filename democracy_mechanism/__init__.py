from otree.api import *
import random

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
    sum_vote = models.IntegerField()
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
    type = models.StringField()
    partner = models.IntegerField()
    kept = models.CurrencyField(
        initial=0
    )


# FUNCTIONS
def set_payoffs(group: Group):
    # Sets payoffs for Senders and Receivers
    for player in group.get_players():
        if player.type == "Sender":
            player.payoff = player.kept
        else:
            partner = group.get_player_by_id(player.partner)
            player.kept = partner.kept
            player.payoff = Constants.endowment - partner.kept


def creating_session(subsession):
    # Assign roles and break into pairs
    players = subsession.get_players()
    random.shuffle(players)
    for i in range(0, len(players), 2):
        players[i].type = 'Sender'
        players[i+1].type = 'Receiver'
        players[i].partner = players[i+1].id_in_group
        players[i+1].partner = players[i].id_in_group

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

        # Determine majority vote
        s = 0
        for p in group.get_players():
            s += p.vote
        group.sum_vote = s
        if s * 2 < Constants.players_per_group:
            group.group_vote = 0  # majority for 0
        elif s * 2 > Constants.players_per_group:
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
        return player.type == "Sender"


class ResultsWaitDictator(WaitPage):
    after_all_players_arrive = set_payoffs


class DictatorResults(Page):
    pass
    @staticmethod
    def vars_for_template(player):
        return dict(kept=player.kept, offer=Constants.endowment - player.kept)


page_sequence = [Voting, ResultsWaitVoting, VotingResults, DictatorOffer, ResultsWaitDictator, DictatorResults]
