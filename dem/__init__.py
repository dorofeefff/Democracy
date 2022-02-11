from otree.api import *
import random

c = Currency

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'dem'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 2
    # Initial amount allocated to the dictator
    ENDOWMENT = cu(1000)
    # The bonus that the guesser gets if correct
    GUESSER_BONUS = cu(500)
    # Default choice set
    DEFAULT_SEND_MIN = cu(200)
    DEFAULT_SEND_MAX = cu(300)
    # Allocations that are added, according to the two modifications
    FAIR_SEND = cu(400)
    SELFISH_SEND = cu(100)
    # Roles
    SENDER_ROLE = 'Individual A'
    RECEIVER_ROLE = 'Individual B'
    GUESSER_ROLE = 'Individual C'


# Useful variables for the dictator stage
dictator_vars = dict(
    endowment=C.ENDOWMENT.__int__(),
    send_min=C.DEFAULT_SEND_MIN.__int__(),
    send_max=C.DEFAULT_SEND_MAX.__int__(),
    send_fair=C.FAIR_SEND.__int__(),
    send_selfish=C.SELFISH_SEND.__int__()
)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # mode defines the type of dictator game (adding a selfish or a fair choice)
    mode = models.StringField(
        initial='"default"'
    )
    # Voting stage
    sum_vote = models.IntegerField()
    group_vote = models.IntegerField()
    overridden = models.BooleanField()
    final_group_choice = models.IntegerField()
    # Dictator stage
    type = models.StringField()
    send = models.CurrencyField()
    keep = models.CurrencyField()
    guess = models.CurrencyField()


class Player(BasePlayer):
    # Voting stage
    vote = models.IntegerField(
        label="What do you want?",
        choices=[[0, "Add fair distribution"], [1, "Add selfish distribution"]]
    )
    # Feedback
    feedback = models.LongStringField()


# FUNCTIONS
def set_payoffs(group: Group):
    sender = group.get_player_by_role(C.SENDER_ROLE)
    receiver = group.get_player_by_role(C.RECEIVER_ROLE)
    guesser = group.get_player_by_role(C.GUESSER_ROLE)

    sender.payoff = group.keep
    receiver.payoff = group.send
    guesser.payoff = int(abs(group.send - group.guess) <= 1) * C.GUESSER_BONUS


def creating_session(subsession):
    subsession.group_randomly()


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
        if s * 2 < C.PLAYERS_PER_GROUP:
            group.group_vote = 0  # majority for 0
        elif s * 2 > C.PLAYERS_PER_GROUP:
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
        return D


class DictatorSend(Page):
    form_model = 'group'
    form_fields = ['send']

    @staticmethod
    def is_displayed(player):
        return player.role == C.SENDER_ROLE

    @staticmethod
    def vars_for_template(player):
        return dictator_vars

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.group.keep = C.ENDOWMENT - player.group.send


class DictatorGuess(Page):

    @staticmethod
    def is_displayed(player):
        return player.role == C.GUESSER_ROLE

    form_model = 'group'
    form_fields = ['guess']

    @staticmethod
    def vars_for_template(player):
        return dictator_vars


class ResultsWaitDictator(WaitPage):
    template_name = 'dem/ResultsWaitDictator.html'
    after_all_players_arrive = set_payoffs
    @staticmethod
    def vars_for_template(player):
        return dict(role=player.role)


class DictatorResults(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            keep=player.group.keep,
            send=player.group.send,
            guess=player.group.guess,
            sender=C.SENDER_ROLE,
            receiver=C.RECEIVER_ROLE,
            guesser=C.GUESSER_ROLE
        )


class Feedback(Page):
    form_model = "player"
    form_fields = ["feedback"]

    @staticmethod
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


# page_sequence = [Voting]


page_sequence = [Voting, ResultsWaitVoting, VotingResults, DictatorSend,
                 DictatorGuess, ResultsWaitDictator, DictatorResults, Feedback]
