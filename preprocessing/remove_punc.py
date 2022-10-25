import re


def remove_punc(text):
    # remove '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    return re.sub(r'[^\w\s]', '', text)
