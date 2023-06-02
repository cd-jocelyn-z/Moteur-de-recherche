'''
    la creation d'un dictionnaire qui contient
    la sous ensemble D des documents qui contient
    au moins au mot de la requete
'''
def sousBdoc(index,requete):
    result={}
    sousBDOC=set()
    tfidf_dico={}
    doc_vector={}

    
    for WordRequete in requete.split(' '):
      for Word in index.keys():
        if WordRequete == Word:
          result[Word]=index.get(WordRequete)

    for word in result.keys():
        for document in result[word].keys():
            if document not in sousBDOC:
                sousBDOC.add(document)
    
    return sousBDOC
