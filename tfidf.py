import math

from tokenization import tokenization

<<<<<<< HEAD
'''
La fonction tfidf prend en entrée le sousBDOC, la matrice tf et l'index. Elle renvoie la matrice tfidf de type
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
=======

def tfidf(bdoc_dict, doc_term_freq, index_dict):
    documents_tfidf_dict = {}

    for document_id in bdoc_dict:
        total_documents = len(bdoc_dict)
        tfidf_inner_dict = {}
        total_tokens_in_document = len(tokenization(bdoc_dict[document_id]))

        for token in doc_term_freq[document_id].keys():
            token_occurrence = doc_term_freq[document_id][token]
            term_frequency = token_occurrence / total_tokens_in_document
            total_documents_containing_the_word = len(index_dict[token])
            idf = math.log10(total_documents / total_documents_containing_the_word)
            tfidf = term_frequency * idf
            tfidf_inner_dict[token] = tfidf

        # normalized_vector
        documents_tfidf_dict[document_id] = tfidf_inner_dict

    return documents_tfidf_dict
>>>>>>> 2b8df62f9ebb07f58cc2ae16cbcacee26df68861
