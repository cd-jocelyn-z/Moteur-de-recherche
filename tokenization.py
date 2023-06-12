import re
import unicodedata


def tokenization(content):
    lowercase_content = content.lower()
    normalized_text = unicodedata.normalize('NFD', lowercase_content)
    diacritic_pattern = re.compile(r'[\u0300-\u036f]')
    text_without_diacritics = diacritic_pattern.sub('', normalized_text)
    tokens = re.split(r'[,()_\"\-:.?\s\']+', text_without_diacritics)

    return tokens