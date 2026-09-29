# text_utils.py - turns a description into a set of keywords

from config import IGNORE_WORDS


def get_keywords(description):
    words = description.lower().split()
    keywords = set()
    for word in words:
        # strip basic punctuation a person might type
        cleaned = word.strip(".,!?")
        if cleaned not in IGNORE_WORDS and cleaned != "":
            keywords.add(cleaned)
    return keywords
