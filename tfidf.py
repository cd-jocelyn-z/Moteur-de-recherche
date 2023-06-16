import math
'''
La fonction tfidf prend en entrée le sousBDOC,
la matrice tf et l'index. Elle renvoie la matrice tfidf de type
dictionnaire de dictionnaire matrice_tfidf = {doc:{mot:tf*idf}}         
'''
def tfidf(sousBDOC,tf,index):
    matrice_tfidf = {}
    for document in sousBDOC:
        N= len(tf)
        tfidf_vecteur = {}
        
        for word in tf[document].keys():
            tf_value = tf[document][word]
            n = len(index[word])
            idf = math.log10(N/n)
            tfidf = tf_value * idf
            tfidf_vecteur[word] = tfidf

        matrice_tfidf[document] =  tfidf_vecteur 
    return matrice_tfidf
