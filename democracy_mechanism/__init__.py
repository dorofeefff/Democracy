from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'democracy_mechanism'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    selected_a = models.BooleanField()


class Player(BasePlayer):
    voted_for_a = models.BooleanField(
        label="What do you want?",
        choices=[[True,"Add fair distribution"],[False,"Add unfair distribution"]]
    )


# PAGES
class Voting(Page):
    form_model = "player"
    form_fields = ["voted_for_a"]


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        votes_for_a = 0
        for p in group.get_players():
            votes_for_a += int(p.voted_for_a)
        if votes_for_a > 1:
            group.selected_a = True
        else:
            group.selected_a = False

class Results(Page):
    form_model = "group"



page_sequence = [Voting, ResultsWaitPage, Results]
