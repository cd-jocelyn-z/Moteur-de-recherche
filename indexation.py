from tokenization import tokenization


<<<<<<< HEAD
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
=======
def indexation(bdoc_dict):
    index_dict = {}
    doc_term_freq = {}

    for doc_id in bdoc_dict.keys():
        term_freq_dict = {}
        for word in tokenization(bdoc_dict[doc_id]):

            if word in term_freq_dict:
                term_freq_dict[word] += 1
            else:
                term_freq_dict[word] = 1

            if word in index_dict:
                if doc_id in index_dict[word]:
                    index_dict[word][doc_id] += 1
                else:
                    index_dict[word][doc_id] = 1
            else:
                index_dict.setdefault(word, {doc_id: 0})

        doc_term_freq[doc_id] = term_freq_dict

    return index_dict, doc_term_freq
>>>>>>> 2b8df62f9ebb07f58cc2ae16cbcacee26df68861
