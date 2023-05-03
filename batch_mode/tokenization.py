import re


def get_tokens(content):
    pattern = r'[,()_\".?\s\']+'
    tokens = re.split(pattern, content)

    tokens = list(set([token.lower() for token in tokens]))

    return tokens
