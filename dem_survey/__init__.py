from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Demographics
    sex = models.StringField(
        label='What is your gender identity?',
        choices=[
            ['female', 'Woman or Female'],
            ['male', 'Man or Male'],
            ['trans_w', 'Trans Woman'],
            ['trans_m', 'Trans Man'],
            ['queer', 'Genderqueer'],
            ['agender', 'Agender'],
            ['genderfluid', 'Genderfluid'],
            ['intersex', 'Intersex'],
            ['non_binary', 'Non-binary'],
            ['other', 'Other'],
        ],
    )
    ethnicity = models.StringField(
        label='How do you usually describe yourself?',
        choices=[
            ['native', 'American Indian or Native Alaskan'],
            ['asian', 'Asian or Asian American'],
            ['black', 'Black or African American'],
            ['hispanic', 'Hispanic or Latino/a/x'],
            ['arab', 'Middle Eastern/North African (MENA) or Arab Origin'],
            ['hawaiian', 'Native Hawaiian or Other Pacific Islander Native'],
            ['white', 'White or Caucasian'],
            ['multi', 'Multiracial or Biracial'],
            ['none', 'None of the above'],
        ],
    )
    age = models.IntegerField(
        label='What is your age?',
        min=10,
        max=99,
    )
    major = models.StringField(
        label='What is your major?',
        choices=[
            ['arts', 'Arts and Media'],
            ['economics', 'Business and Economics'],
            ['education', 'Education'],
            ['health', 'Health'],
            ['humanities', 'Humanities'],
            ['stem', 'Science, Technology, Engineering & Math'],
            ['social', 'Social Sciences (other than economics)'],
            ['other', 'Other'],
        ],
    )
    country_of_birth = models.StringField(
        label='In which country were you born?',
        choices=[
            ["Afghanistan", "Afghanistan"],
            ["Albania", "Albania"],
            ["Algeria", "Algeria"],
            ["Andorra", "Andorra"],
            ["Angola", "Angola"],
            ["Antigua and Barbuda", "Antigua and Barbuda"],
            ["Argentina", "Argentina"],
            ["Armenia", "Armenia"],
            ["Australia", "Australia"],
            ["Austria", "Austria"],
            ["Azerbaijan", "Azerbaijan"],
            ["Bahamas", "Bahamas"],
            ["Bahrain", "Bahrain"],
            ["Bangladesh", "Bangladesh"],
            ["Barbados", "Barbados"],
            ["Belarus", "Belarus"],
            ["Belgium", "Belgium"],
            ["Belize", "Belize"],
            ["Benin", "Benin"],
            ["Bhutan", "Bhutan"],
            ["Bolivia", "Bolivia"],
            ["Bosnia and Herzegovina", "Bosnia and Herzegovina"],
            ["Botswana", "Botswana"],
            ["Brazil", "Brazil"],
            ["Brunei ", "Brunei "],
            ["Bulgaria", "Bulgaria"],
            ["Burkina Faso", "Burkina Faso"],
            ["Burundi", "Burundi"],
            ["Côte d'Ivoire", "Côte d'Ivoire"],
            ["Cabo Verde", "Cabo Verde"],
            ["Cambodia", "Cambodia"],
            ["Cameroon", "Cameroon"],
            ["Canada", "Canada"],
            ["Central African Republic", "Central African Republic"],
            ["Chad", "Chad"],
            ["Chile", "Chile"],
            ["China", "China"],
            ["Colombia", "Colombia"],
            ["Comoros", "Comoros"],
            ["Congo (Congo-Brazzaville)", "Congo (Congo-Brazzaville)"],
            ["Costa Rica", "Costa Rica"],
            ["Croatia", "Croatia"],
            ["Cuba", "Cuba"],
            ["Cyprus", "Cyprus"],
            ["Czech Republic", "Czech Republic"],
            ["Democratic Republic of the Congo", "Democratic Republic of the Congo"],
            ["Denmark", "Denmark"],
            ["Djibouti", "Djibouti"],
            ["Dominica", "Dominica"],
            ["Dominican Republic", "Dominican Republic"],
            ["Ecuador", "Ecuador"],
            ["Egypt", "Egypt"],
            ["El Salvador", "El Salvador"],
            ["Equatorial Guinea", "Equatorial Guinea"],
            ["Eritrea", "Eritrea"],
            ["Estonia", "Estonia"],
            ["Eswatini", "Eswatini"],
            ["Ethiopia", "Ethiopia"],
            ["Fiji", "Fiji"],
            ["Finland", "Finland"],
            ["France", "France"],
            ["Gabon", "Gabon"],
            ["Gambia", "Gambia"],
            ["Georgia", "Georgia"],
            ["Germany", "Germany"],
            ["Ghana", "Ghana"],
            ["Greece", "Greece"],
            ["Grenada", "Grenada"],
            ["Guatemala", "Guatemala"],
            ["Guinea", "Guinea"],
            ["Guinea-Bissau", "Guinea-Bissau"],
            ["Guyana", "Guyana"],
            ["Haiti", "Haiti"],
            ["Holy See", "Holy See"],
            ["Honduras", "Honduras"],
            ["Hungary", "Hungary"],
            ["Iceland", "Iceland"],
            ["India", "India"],
            ["Indonesia", "Indonesia"],
            ["Iran", "Iran"],
            ["Iraq", "Iraq"],
            ["Ireland", "Ireland"],
            ["Israel", "Israel"],
            ["Italy", "Italy"],
            ["Jamaica", "Jamaica"],
            ["Japan", "Japan"],
            ["Jordan", "Jordan"],
            ["Kazakhstan", "Kazakhstan"],
            ["Kenya", "Kenya"],
            ["Kiribati", "Kiribati"],
            ["Kuwait", "Kuwait"],
            ["Kyrgyzstan", "Kyrgyzstan"],
            ["Laos", "Laos"],
            ["Latvia", "Latvia"],
            ["Lebanon", "Lebanon"],
            ["Lesotho", "Lesotho"],
            ["Liberia", "Liberia"],
            ["Libya", "Libya"],
            ["Liechtenstein", "Liechtenstein"],
            ["Lithuania", "Lithuania"],
            ["Luxembourg", "Luxembourg"],
            ["Madagascar", "Madagascar"],
            ["Malawi", "Malawi"],
            ["Malaysia", "Malaysia"],
            ["Maldives", "Maldives"],
            ["Mali", "Mali"],
            ["Malta", "Malta"],
            ["Marshall Islands", "Marshall Islands"],
            ["Mauritania", "Mauritania"],
            ["Mauritius", "Mauritius"],
            ["Mexico", "Mexico"],
            ["Micronesia", "Micronesia"],
            ["Moldova", "Moldova"],
            ["Monaco", "Monaco"],
            ["Mongolia", "Mongolia"],
            ["Montenegro", "Montenegro"],
            ["Morocco", "Morocco"],
            ["Mozambique", "Mozambique"],
            ["Myanmar", "Myanmar"],
            ["Namibia", "Namibia"],
            ["Nauru", "Nauru"],
            ["Nepal", "Nepal"],
            ["Netherlands", "Netherlands"],
            ["New Zealand", "New Zealand"],
            ["Nicaragua", "Nicaragua"],
            ["Niger", "Niger"],
            ["Nigeria", "Nigeria"],
            ["North Korea", "North Korea"],
            ["North Macedonia", "North Macedonia"],
            ["Norway", "Norway"],
            ["Oman", "Oman"],
            ["Pakistan", "Pakistan"],
            ["Palau", "Palau"],
            ["Palestine State", "Palestine State"],
            ["Panama", "Panama"],
            ["Papua New Guinea", "Papua New Guinea"],
            ["Paraguay", "Paraguay"],
            ["Peru", "Peru"],
            ["Philippines", "Philippines"],
            ["Poland", "Poland"],
            ["Portugal", "Portugal"],
            ["Qatar", "Qatar"],
            ["Romania", "Romania"],
            ["Russia", "Russia"],
            ["Rwanda", "Rwanda"],
            ["Saint Kitts and Nevis", "Saint Kitts and Nevis"],
            ["Saint Lucia", "Saint Lucia"],
            ["Saint Vincent and the Grenadines", "Saint Vincent and the Grenadines"],
            ["Samoa", "Samoa"],
            ["San Marino", "San Marino"],
            ["Sao Tome and Principe", "Sao Tome and Principe"],
            ["Saudi Arabia", "Saudi Arabia"],
            ["Senegal", "Senegal"],
            ["Serbia", "Serbia"],
            ["Seychelles", "Seychelles"],
            ["Sierra Leone", "Sierra Leone"],
            ["Singapore", "Singapore"],
            ["Slovakia", "Slovakia"],
            ["Slovenia", "Slovenia"],
            ["Solomon Islands", "Solomon Islands"],
            ["Somalia", "Somalia"],
            ["South Africa", "South Africa"],
            ["South Korea", "South Korea"],
            ["South Sudan", "South Sudan"],
            ["Spain", "Spain"],
            ["Sri Lanka", "Sri Lanka"],
            ["Sudan", "Sudan"],
            ["Suriname", "Suriname"],
            ["Sweden", "Sweden"],
            ["Switzerland", "Switzerland"],
            ["Syria", "Syria"],
            ["Tajikistan", "Tajikistan"],
            ["Tanzania", "Tanzania"],
            ["Thailand", "Thailand"],
            ["Timor-Leste", "Timor-Leste"],
            ["Togo", "Togo"],
            ["Tonga", "Tonga"],
            ["Trinidad and Tobago", "Trinidad and Tobago"],
            ["Tunisia", "Tunisia"],
            ["Turkey", "Turkey"],
            ["Turkmenistan", "Turkmenistan"],
            ["Tuvalu", "Tuvalu"],
            ["Uganda", "Uganda"],
            ["Ukraine", "Ukraine"],
            ["United Arab Emirates", "United Arab Emirates"],
            ["United Kingdom", "United Kingdom"],
            ["United States of America", "United States of America"],
            ["Uruguay", "Uruguay"],
            ["Uzbekistan", "Uzbekistan"],
            ["Vanuatu", "Vanuatu"],
            ["Venezuela", "Venezuela"],
            ["Vietnam", "Vietnam"],
            ["Yemen", "Yemen"],
            ["Zambia", "Zambia"],
            ["Zimbabwe", "Zimbabwe"],
            ["Other / Country not listed", "Other / Country not listed"],
    ],
    )

    # Exit Survey
    exit1 = models.LongStringField(
        label='If you ever were Individual A, why did you choose to allocate the specific amount to Individual B?'
    )
    exit2 = models.LongStringField(
        label='If you ever were Individual C, what influenced your guess?'
    )
    exit3 = models.LongStringField(
        label='Why did you vote for Modifications 1 or 2?'
    )
    exit4 = models.LongStringField(
        label='If your vote was ever overridden, how did this affect your behavior?'
    )
    exit5 = models.LongStringField(
        label='Did your behavior change when the same Modification was selected by voting as opposed to randomly selected after votes were overridden?'
    )

    # World Value Survey

    # TRUST TO PEOPLE
    wvs_57 = models.IntegerField(
        label='Generally speaking, would you say that most people can be trusted or that you need to be very careful in dealing with people?',
        choices=[[1, 'Most people can be trusted'], [0, 'Need to be very careful']]
    )
    wvs_60 = models.IntegerField(
        label='How much do you trust people you know personally?',
        choices=[[0, 'Do not trust at all'], [1, 'Do not trust very much'], [2, 'Trust somewhat'], [3, 'Trust completely']]
    )
    wvs_61 = models.IntegerField(
        label='How much do you trust people you meet for the first time?',
        choices=[[0, 'Do not trust at all'], [1, 'Do not trust very much'], [2, 'Trust somewhat'], [3, 'Trust completely']]
    )

    # AGENCY
    wvs_48 = models.IntegerField(
        label='Some people feel they have completely free choice and control over their lives, while other people feel that what they do has no real effect on what happens to them. Please use this scale where 1 means "no choice at all" and 10 means "a great deal of choice" to indicate how much freedom of choice and control you feel you have over the way your life turns out.',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
    # Do you agree with the following statements?
    wvs_110_1 = models.IntegerField(
        label='In the long run, hard work usually brings a better life',
        choices=[[0, 'Strongly disagree'], [1, 'Disagree'], [2, 'Agree'], [3, 'Strongly agree']]
    )
    wvs_110_2 = models.IntegerField(
        label="Hard work doesn't generally bring success—it’s more a matter of luck and connections",
        choices=[[0, 'Strongly disagree'], [1, 'Disagree'], [2, 'Agree'], [3, 'Strongly agree']]
    )

    # TRUST TO INSTITUTIONS
    # How much confidence you have in the following organizations?
    wvs_66 = models.IntegerField(
        label='The press',
        choices=[[0, 'None at all'], [1, 'Not very much'], [2, 'Quite a lot'], [3, 'A great deal']]
    )
    wvs_69 = models.IntegerField(
        label='The police',
        choices=[[0, 'None at all'], [1, 'Not very much'], [2, 'Quite a lot'], [3, 'A great deal']]
    )
    wvs_71 = models.IntegerField(
        label='The government',
        choices=[[0, 'None at all'], [1, 'Not very much'], [2, 'Quite a lot'], [3, 'A great deal']]
    )

    # ATTITUDES TOWARDS ELECTIONS
    # When elections take place, do you vote always, usually or never? Please tell me separately for each of the following levels
    wvs_221 = models.IntegerField(
        label='Local level',
        choices=[[-1, 'Not allowed to vote'], [0, 'Never'], [1, 'Usually'], [2, 'Always']]
    )
    wvs_222 = models.IntegerField(
        label='National level',
        choices=[[-1, 'Not allowed to vote'], [0, 'Never'], [1, 'Usually'], [2, 'Always']]
    )

    # In your view, how often do the following things occur in this country’s elections?
    wvs_224 = models.IntegerField(
        label='Votes are counted fairly',
        choices=[[0, 'Not at all often'], [1, 'Not often'], [2, 'Fairly often'], [3, 'Very often']]
    )
    wvs_225 = models.IntegerField(
        label='Opposition candidates are prevented from running',
        choices=[[0, 'Not at all often'], [1, 'Not often'], [2, 'Fairly often'], [3, 'Very often']]
    )
    wvs_230 = models.IntegerField(
        label='Rich people buy elections',
        choices=[[0, 'Not at all often'], [1, 'Not often'], [2, 'Fairly often'], [3, 'Very often']]
    )
    wvs_232 = models.IntegerField(
        label='Voters are offered a genuine choice in the elections',
        choices=[[0, 'Not at all often'], [1, 'Not often'], [2, 'Fairly often'], [3, 'Very often']]
    )

    wvs_234 = models.IntegerField(
        label='Some people think that having honest elections makes a lot of difference in their lives; other people think that it doesn’t matter much. How important would you say is having honest elections for you?',
        choices=[[0, 'Not at all important'], [1, 'Not very important'], [2, 'Rather important'], [3, 'Very important']]
    )

    # ATTITUDES TOWARDS DEMOCRACY
    # For each of the following political systems, would you say it is a very good, fairly good, fairly bad or very bad way of governing this country?
    wvs_235 = models.IntegerField(
        label='Having a strong leader who does not have to bother with parliament and elections',
        choices=[[0, 'Very bad'], [1, 'Fairly bad'], [2, 'Fairly good'], [3, 'Very good']]
    )
    wvs_236 = models.IntegerField(
        label='Having experts, not government, make decisions according to what they think is best for the country',
        choices=[[0, 'Very bad'], [1, 'Fairly bad'], [2, 'Fairly good'], [3, 'Very good']]
    )
    wvs_238 = models.IntegerField(
        label='Having a democratic political system',
        choices=[[0, 'Very bad'], [1, 'Fairly bad'], [2, 'Fairly good'], [3, 'Very good']]
    )

    wvs_250 = models.IntegerField(
        label='How important is it for you to live in a country that is governed democratically? On this scale where 1 means it is “not at all important” and 10 means “absolutely important” what position would you choose?',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['sex', 'ethnicity', 'age', 'major', 'country_of_birth']


class ExitSurvey(Page):
    form_model = 'player'
    form_fields = ['exit1', 'exit2', 'exit3', 'exit4', 'exit5']


class WVS1(Page):
    form_model = 'player'
    form_fields = ['wvs_221', 'wvs_222', 'wvs_224', 'wvs_225', 'wvs_230', 'wvs_232', 'wvs_234']


class WVS2(Page):
    form_model = 'player'
    form_fields = ['wvs_235', 'wvs_236', 'wvs_238', 'wvs_250']


class WVS3(Page):
    form_model = 'player'
    form_fields = ['wvs_48', 'wvs_110_1', 'wvs_110_2', 'wvs_66', 'wvs_69', 'wvs_71']


page_sequence = [ExitSurvey, WVS1, WVS2, WVS3, Demographics]
