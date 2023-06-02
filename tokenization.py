import re



def tokenization(content):
    
    tokens=re.split(r'[,()_\"\-:.?\s\']+',content)
    lowercase_tokens = [token.lower() for token in tokens]

    return lowercase_tokens





