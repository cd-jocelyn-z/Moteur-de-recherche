import re

def indexation(BDOC):
    index={}

    for NumArticle in BDOC.keys():
      dic2={}
      for word in re.split(r'[,()_\".?\s\']+',BDOC[NumArticle]):
        word=word.lower()
        if word not in index.keys():
          dic2={NumArticle:0}
          index[word]=dic2
        if word in index.keys():
          if NumArticle in index[word].keys():
            index[word][NumArticle]+=1
          else:
            index[word][NumArticle]=1

    return index
