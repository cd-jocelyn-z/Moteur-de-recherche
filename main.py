import readfile
import re

print("reading the content of the files.....")
BDOC = readfile.readfile(".\\AMARYLLIS-98-extrait-OFIL 2\\OFIL\\OD1")
print("end of reading")

## PHASE D'INDEXATION

index={}

for NumArticle in BDOCtest.keys():
  dic2={}
  for word in re.split(r'[,.?\s\']+',BDOC[NumArticle]):
    if word not in index.keys():
      dic2={NumArticle:0}
      index[word]=dic2
    if word in index.keys():
      if NumArticle in index[word].keys():
        index[word][NumArticle]+=1
      else:
        index[word][NumArticle]=1

        
print("le mot 'il'")
print(index["il"])

## PHASE D'INTERROGATION

requete="Algeria economic"
result={}
for WordRequete in requete.split(' '):
  print(WordRequete)
  for Word in index.keys():
    if WordRequete == Word:
      result[Word]=index.get(WordRequete)

#print(result)



