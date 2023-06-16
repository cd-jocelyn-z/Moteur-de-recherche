import math

'''
Vectorisation de la requête:
La fonction requete_vecteur prend en entrée la requête, l'index ainsi que la matrice tf. Elle renvoie la requête vectorisée sous forme 
de dictionnaire req = {mot_requete:tf*idf}.
'''

def requete_vecteur(requete,index,tf):
    N= len(tf)
    req={}
    
    for word in requete:
        
        if word in index.keys():
            tf = requete.count(word)
            n = len(index[word])
            idf = math.log10(N/n)
            tfidf = tf * idf
            req[word] = tfidf
            
        else:
            print(f"Le mot {word} n'est pas dans le corpus")
    
    print(f"Le vecteur de requete est : {req}")
    return req 
