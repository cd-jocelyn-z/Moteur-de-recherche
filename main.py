import readfile

'''
    an indexion function using only a list of two elements.
    These elements are two textes imitating the role of documents and the BDOC is the database.
    BDOC ==> a list 
    doc1 and doc2 ==> docs
'''
doc1='Algeria is a North African country with a rich history and diverse culture. Its capital is Algiers, which is known for its beautiful architecture and bustling markets. Algeria is the largest country in Africa and has a population of over 43 million people. The country is home to a variety of landscapes, from the Sahara Desert to the Mediterranean coastline, and has a unique blend of Arabic, Berber, and French influences in its culture and language.'
doc2="Algeria gained independence from France in 1962, after a long and difficult struggle. Since then, the country has undergone significant political and economic changes, including a civil war in the 1990s. However, Algeria has also made significant progress in areas such as education, healthcare, and women's rights. The country is known for its rich cultural heritage, including traditional music and dance, and its beautiful handicrafts such as pottery, textiles, and jewelry. Despite the challenges it has faced, Algeria remains a vibrant and diverse country with a lot to offer."
BDOC=[doc1,doc2]


## PHASE D'INDEXATION

index={}
for NumDoc,doc in enumerate(BDOC):
  dic2={}
  for word in doc.split(" "):
    if word not in index.keys():
      dic2={NumDoc:0}
      index[word]=dic2
    if word in index.keys():
      if NumDoc in index[word].keys():
        index[word][NumDoc]+=1
      else:
        index[word][NumDoc]=1

## PHASE D'INTERROGATION

requete="Algeria economic"
result={}
for WordRequete in requete.split(' '):
  print(WordRequete)
  for Word in index.keys():
    if WordRequete == Word:
      result[Word]=index.get(WordRequete)

print(result)



