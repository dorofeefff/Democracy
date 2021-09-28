from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pris_new'
    players_per_group = None
    num_rounds = 2
    payoff_CC = -1
    payoff_DD = -3
    payoff_CD = -4
    payoff_DC = 0


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    defect = models.BooleanField(
        label="Choose your action",
        choices=[[True,"Defect"],[False,"Cooperate"]]
    )


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = ["defect"]


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        if player_1.defect:
            if player_2.defect:
                player_1.payoff = Constants.payoff_DD
                player_2.payoff = Constants.payoff_DD
            else:
                player_1.payoff = Constants.payoff_DC
                player_2.payoff - Constants.payoff_CD
        else:
            if player_2.defect:
                player_1.payoff = Constants.payoff_CD
                player_2.payoff = Constants.payoff_DC
            else:
                player_1.payoff = Constants.payoff_CC
                player_2.payoff - Constants.payoff_CC

class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
