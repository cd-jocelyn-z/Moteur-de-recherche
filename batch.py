import batch_functions as bf



def batch_mode(index,tf,nlp):

    Réponse1 = input("Pour une évaluation générale du moteur de recherche, tapez 'G'.\nPour l'évaluation d'une seule requête, tapez 'm'\n").lower()
    
    if Réponse1 == "g":
        bf.evaluation_G(index,tf,nlp) #Effectue l'évalutation générale
    
    
    elif Réponse1 == "m":
        bf.evaluation_micro(index,tf,nlp) #Effectue l'évaluation pour une requête précise
            
    else:
        print("Réponse invalide")
        
