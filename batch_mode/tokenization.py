import re


def get_tokens(content):
    pattern = r'[,()_\".?\s\']+'
    tokens = re.split(pattern, content)

    return tokens
