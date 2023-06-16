


'''
Création du set sousBDOC qui contient le sous-ensemble des documents dans lesquels il y a au moins 1 mot de la requête:
'''
def sousBdoc(index,requete):
  result={}
  sousBDOC=set()
    
  for Word_query in requete:
    for Word in index.keys():
      if Word_query == Word:
        result[Word_query]=index[Word_query]

  for word in result.keys():
    for document in result[word].keys():
      if document not in sousBDOC:
        sousBDOC.add(document)
    
    return sousBDOC
