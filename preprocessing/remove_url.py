import re


def remove_url(text):
    url_pattern = re.compile(r'https?://\S+')
    return url_pattern.sub(r'', text)
