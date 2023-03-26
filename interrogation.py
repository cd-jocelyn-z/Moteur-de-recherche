## PHASE D'INTERROGATION
def interrogation(index,requete):
    requete="france italie"
    result={}
    for WordRequete in requete.split(' '):
      for Word in index.keys():
        if WordRequete == Word:
          result[Word]=index.get(WordRequete)
    return result
