import tokenization

def vocabulaire(sousBDOC:set,BDOC):
    vocabulaire = set()
    for document in sousBDOC:
        tokens = tokenization.tokenization(BDOC[document])
        
        vocabulaire.update(set(tokens))
    return vocabulaire
    
