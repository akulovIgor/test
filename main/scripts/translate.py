import requests
from . import constants


def detect_text(text):
    URL = constants.url_detect
    KEY = constants.translate_token
    TEXT = text

    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'hint': ['en', 'ru']})
    return eval(r.text)


# language = detect_text('Ότι μὲν ὑμει̃σ, ὠ̃ ἄνδρες \'Αθηναι̃οι, πεπόνθατε')['lang']
# print(str(language))


def get_translate(text, lang):
    URL = constants.url_translate
    KEY = constants.translate_token
    TEXT = text
    LANG = lang

    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})
    return eval(r.text)
