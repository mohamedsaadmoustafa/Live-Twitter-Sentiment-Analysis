import re


def remove_handle(text):
    handle_pattern = '@[^\s]+'
    return re.sub(handle_pattern, '', text)  # return text without @handle
