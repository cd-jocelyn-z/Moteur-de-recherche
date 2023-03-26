import readfile

import indexation
import tf


print("reading the content of the files.....")
BDOC = readfile.readfile(".\\AMARYLLIS-98-extrait-OFIL 2\\OFIL\\OD1")
print("end of reading")

## PHASE D'INDEXATION

index=indexation.indexation(BDOC)

print(tf.tf(index,"mail"))


## PHASE D'INTERROGATION

requete="france italie"
result={}
for WordRequete in requete.split(' '):
  for Word in index.keys():
    if WordRequete == Word:
      result[Word]=index.get(WordRequete)

#print(result)



