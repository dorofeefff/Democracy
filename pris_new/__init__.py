from otree.api import *

c = Currency

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'pris_new'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
    PAYOFF_CC = -1
    PAYOFF_DD = -3
    PAYOFF_CD = -4
    PAYOFF_DC = 0


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
                player_1.payoff = C.PAYOFF_DD
                player_2.payoff = C.PAYOFF_DD
            else:
                player_1.payoff = C.PAYOFF_DC
                player_2.payoff - C.PAYOFF_CD
        else:
            if player_2.defect:
                player_1.payoff = C.PAYOFF_CD
                player_2.payoff = C.PAYOFF_DC
            else:
                player_1.payoff = C.PAYOFF_CC
                player_2.payoff - C.PAYOFF_CC

class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
