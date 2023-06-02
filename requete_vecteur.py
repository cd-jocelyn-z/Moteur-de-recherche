import tokenization as tk
import math

'''
        la creation d'un vecteur requete  
        le retour de cette fonction est un dictionnaire:
           req = {
                        mot_requete: tf-idf
                        mot_requete: tf-idf
                        ....
                        motn: tf-idf
                    {
'''

def requete_vecteur(requete,sousBDOC,index):
    
    N= len(sousBDOC)
    req={}
    taille_requete = len(tk.tokenization(requete))
    
    for word in tk.tokenization(requete):
        
        if word in index.keys():
            
            idf = math.log(N/len(index[word]))
            tfidf=(1/taille_requete)* idf
            req[word]=tfidf
            
        else:
            print("une autre requete!")
   
   
    return req 
