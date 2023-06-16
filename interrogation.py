from sousbdoc import sousBdoc
import tokenization as tk
import math
from tfidf import tfidf
from requete_vecteur import requete_vecteur


'''
La fonction cosine_similarity prend en entrée le vecteur requête et l'ensemble des vecteurs documents (contenus dans matrice_tfidf).
Elle envoie un dictionnaire qui contient le numéro du document et sa similarité cosinus avec la requête.
'''

def cosine_similarity(query_vector, document_vectors):
    similarities = {}

    for document_id, document_vector in document_vectors.items():
        dot_product = 0.0
        query_norm = 0.0
        document_norm = 0.0

        # Calcul du produit scalaire entre le vecteur requête et le vecteur document
        for term, query_weight in query_vector.items():
            if term in document_vector:
                dot_product += query_weight * document_vector[term]

            query_norm += query_weight ** 2

        for term, document_weight in document_vector.items():
            document_norm += document_weight ** 2

        #Calcul de la norme du vecteur requête et du vecteur document
        query_norm = math.sqrt(query_norm)
        document_norm = math.sqrt(document_norm)

        # Calcul de la similarité cosinus
        similarity = dot_product / (query_norm * document_norm)

        similarities[document_id] = similarity

    return similarities


def interrogation(requete,index,tf,nlp):
    
    # Tokenization de la requête et suppression des stop words
    tokens = tk.tokenization(requete)
    stop_words = nlp.Defaults.stop_words
    stop_words = set(stop_words).union('-','d','l','s','m','t')
    
    requete = tk.delete_stop_words(tokens,stop_words)
    
    #Création du sousBDOC
    sousBDOC = sousBdoc(index,requete)

    #Création de la matrice tf-idf
    tfidf_matrice= tfidf(sousBDOC,tf,index)
    
    #Vectorisation de la requête
    req = requete_vecteur(requete,index,tf)
    
    #On assigne à "similarite" le dictionnaire {doc_id:similarité}
    similarite = cosine_similarity(req, tfidf_matrice)
    
    #On classe les documents par ordre de similarité
    similarities = {}
    sorted_documents = sorted(similarite.items(), key=lambda x: x[1], reverse=True)
    
    #On décide de ne garder qu'un certain nombre de documents. Ce nombre est spécifié dans sorted_documents[:n]
    for document_id, similarity in sorted_documents[:30]:
        
        similarities[document_id]=similarity
        #print(f"Document: {document}, Similarity: {similarity}")
    
    return similarities
