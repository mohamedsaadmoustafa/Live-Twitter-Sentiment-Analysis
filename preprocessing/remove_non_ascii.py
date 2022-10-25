import re


def remove_non_ascii(text):
    """
        Remove non-ASCII characters
    """
    return re.sub(r'[^\x00-\x7f]', r'', text)
    # return ''.join([x for x in text if x in string.printable])
