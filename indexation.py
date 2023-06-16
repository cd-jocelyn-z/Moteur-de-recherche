import tokenization as tk


'''
La fonction indexation prend en entrée le BDOC et renvoie l'index de type dictionnaire de dictionnaire {mot:{doc:nb_occ}}
ainsi que la matrice tf {doc:{mot:nb_occ}}                                                                 
'''
def indexation(BDOC): 
    index = {} 
    matrice_tf = {}

    for NumArticle in BDOC.keys():

        tf_dict = {}

        words= tk.tokenization(BDOC[NumArticle])
        unique_words = set(words)

        #Création de l'index
        for word in unique_words:            
            if word not in index:
                index[word] = {}
            index[word][NumArticle]=words.count(word)
                
        
        #Création de la matrice tf
        for word in words:
            if word in tf_dict.keys():
                tf_dict[word]+=1
            else:
                tf_dict[word]=1

        matrice_tf[NumArticle]=tf_dict
        
    return index,matrice_tf
