from os import environ


SESSION_CONFIGS = [
    dict(
        name='dem_u',
        display_name="Democracy Ultimatum",
        app_sequence=[
            'dem_ult',
            'dem_survey',
            'payment_info'
        ],
        num_demo_participants=3,
        use_browser_bots=False,
        votes_revealed=False,
        ultimatum=True,
    ),
    dict(
        name='dem_t',
        display_name="Democracy Treatment",
        app_sequence=[
            'dem',
            'dem_survey',
            'payment_info'
        ],
        num_demo_participants=3,
        use_browser_bots=False,
        votes_revealed=True,
        ultimatum=False,
    ),
    dict(
        name='dem_b',
        display_name="Democracy Baseline",
        app_sequence=[
            'dem',
            'dem_survey',
            'payment_info'
        ],
        num_demo_participants=3,
        use_browser_bots=False,
        votes_revealed=False,
        ultimatum=False,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1/330, participation_fee=7.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ROOMS = [
    dict(
        name='TU_LAB',
        display_name='TU LAB',
        participant_label_file='tu_lab.txt',
        use_secure_urls=False,
    )
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'password'

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '3581948518453'

INSTALLED_APPS = ['otree']
