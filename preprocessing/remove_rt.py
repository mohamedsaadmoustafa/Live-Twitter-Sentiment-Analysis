import re


def remove_rt(text):
    # ([RT]) : Remove "RT" from the tweet
    url_pattern = re.compile(r'([RT])')
    return url_pattern.sub(r'', text)
