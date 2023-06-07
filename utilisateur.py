import readfile
import indexation
import interrogation
import os





print("reading the content of the files.....")
file_path = os.path.join(os.curdir, "AMARYLLIS-98-extrait-OFIL 2", "OFIL", "OD1")
BDOC = readfile.readfile(file_path)
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






        
    

        
     


        
