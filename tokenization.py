import re

def tokenization(content):
    
    tokens=re.split(r'[,()_\".?\s\']+',content)

    return tokens
