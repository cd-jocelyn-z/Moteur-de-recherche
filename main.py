import os
from readfile import readfile
from indexation import indexation
from interrogation import interrogation
import pickle
from batch import batch_mode
import spacy


'''Sérialisation de l'index et de la matrice tf'''
#Dans le cas où le fichier sérialisé est dans le répertoire courant
if  "serialized_index.pickle" in os.listdir(os.curdir): 
    with open('serialized_index.pickle', 'rb') as f:
        serialized_index = f.read()
    index = pickle.loads(serialized_index) #Assignation de l'index sérialisé à "index"
    with open('serialized_tf.pickle', 'rb') as f:
        serialized_tf = f.read() 
    tf = pickle.loads(serialized_tf) #Assignation de la matrice tf sérialisée à "tf"
    
else:  
   #Dans le cas où le fichier sérialisé n'existe pas ou qu'il n'est pas le dans répertoire courant
    BDOC = readfile(os.path.join(os.curdir, "AMARYLLIS-98-extrait-OFIL", "OFIL", "OD1"))
    index,tf=indexation(BDOC)

    serialized_index = pickle.dumps(index)
    with open('serialized_index.pickle', 'wb') as f:
        f.write(serialized_index)
    
    serialized_tf = pickle.dumps(tf)
    with open('serialized_tf.pickle', 'wb') as f:
        f.write(serialized_tf)


'''Chargement du modèle spaCy pour le français'''
nlp = spacy.load("fr_core_news_sm")

while True:
    Rep = input("Tapez R pour entrer une requête. Tapez B pour entrer dans le batch mode.\nTapez Q pour quitter.\n").lower()
    if Rep == "r":
        requete = input("Entrez la requete : ").lower()

    ## PHASE D'INTERROGATION

        similarities = interrogation(requete,index,tf,nlp)

        for article,similarity in similarities.items():
            print(f"Article numéro : {article} Similarité cosinus : {similarity}")
            
    ## BATCH MODE
    elif Rep == "b":
        batch_mode(index,tf,nlp)
        
    elif Rep == "q":
        print("Au revoir")
        break
    else:
        print("Réponse invalide")