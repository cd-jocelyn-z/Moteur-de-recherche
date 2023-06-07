import readfile
import indexation
import interrogation






print("reading the content of the files.....")
BDOC = readfile.readfile(".\\AMARYLLIS-98-extrait-OFIL 2\\OFIL\\OD1")
print("end of reading")




## PHASE D'INDEXATION
'''
    dictionnaire {  clé    : mot
                    valeur : dictionaire : {
                                                clé : documentID
                                                valeur : tf }
                                }                                      
'''
index,tf=indexation.indexation(BDOC)
#print(index["batna"])


while True:
    requete = input("entrez la requete ")

    ## PHASE D'INTERROGATION

    similarities = interrogation.interrogation(requete,BDOC,index,tf)

    print(similarities)






        
    

        
     


        
