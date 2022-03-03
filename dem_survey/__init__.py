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


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['sex', 'ethnicity', 'age', 'major', 'country_of_birth']


class ExitSurvey(Page):
    form_model = 'player'
    form_fields = ['exit1', 'exit2', 'exit3', 'exit4', 'exit5']


page_sequence = [ExitSurvey, Demographics]
