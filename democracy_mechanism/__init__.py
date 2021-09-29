from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'democracy_mechanism'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # Voting stage
    group_choice = models.BooleanField()
    overridden = models.BooleanField()
    final_choice = models.BooleanField()
    # Dictator stage



class Player(BasePlayer):
    vote = models.BooleanField(
        label="What do you want?",
        choices=[[True, "Add fair distribution"], [False, "Add unfair distribution"]]
    )


# PAGES
class Voting(Page):
    form_model = "player"
    form_fields = ["vote"]


class ResultsWaitPage(WaitPage):
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


page_sequence = [Voting, ResultsWaitPage, VotingResults]
