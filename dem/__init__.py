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
    DEFAULT_ALLOCATION_MIN = cu(200)
    DEFAULT_ALLOCATION_MAX = cu(300)
    # Allocations that are added, according to the two modifications
    FAIR_ALLOCATION = cu(400)
    SELFISH_ALLOCATION = cu(100)
    # Roles
    SENDER_ROLE = 'Individual A'
    RECEIVER_ROLE = 'Individual B'
    GUESSER_ROLE = 'Individual C'


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
    kept = models.CurrencyField()
    sent = models.CurrencyField()
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

    sender.payoff = group.kept
    receiver.payoff = group.sent
    guesser.payoff = int(abs(group.sent - group.guess) <= 1) * C.GUESSER_BONUS


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
        return dict(
            selfish_vote=player.group.sum_vote,
            fair_vote=C.PLAYERS_PER_GROUP - player.group.sum_vote,
            group_vote=translate[player.group.group_vote],
            overridden=player.group.overridden,
            final=translate[player.group.final_group_choice]
        )


class DictatorSend(Page):
    form_model = 'group'
    form_fields = ['sent']

    @staticmethod
    def is_displayed(player):
        return player.role == C.SENDER_ROLE

    @staticmethod
    def vars_for_template(player):
        return dict(
            fair_option=6,
            selfish_option=9,
            endowment=C.ENDOWMENT.__int__(),
            send_min=C.DEFAULT_ALLOCATION_MIN.__int__(),
            send_max=C.DEFAULT_ALLOCATION_MAX.__int__(),
            send_fair=C.FAIR_ALLOCATION.__int__(),
            send_selfish=C.SELFISH_ALLOCATION.__int__()
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.group.kept = C.ENDOWMENT - player.group.sent


class DictatorGuess(Page):

    @staticmethod
    def is_displayed(player):
        return player.role == C.GUESSER_ROLE

    form_model = 'group'
    form_fields = ['guess']


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
            kept=player.group.kept,
            guess=player.group.guess,
            offer=C.ENDOWMENT - player.group.kept,
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
