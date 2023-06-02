import readfile
import indexation
import interrogation
import sousbdoc
import tokenization as tk
import vocabulaire
import math
import tfidf
import requete_vecteur


'''
    fonction pour calculer la similarité 
'''
def calculate_similarity(req, dictionnaire):
    similarity_scores = {}
    req_vector = req.values()

    for doc_id, doc in dictionnaire.items():
        doc_vector = doc.values()

        # Calculate dot product
        dot_product = sum(req_value * doc_value for req_value, doc_value in zip(req_vector, doc_vector))

        # Calculate Euclidean norm
        req_norm = math.sqrt(sum(value**2 for value in req_vector))
        doc_norm = math.sqrt(sum(value**2 for value in doc_vector))

        # Calculate cosine similarity
        similarity = dot_product / (req_norm * doc_norm)

        similarity_scores[doc_id] = similarity

    return similarity_scores



def interrogation(requete,BDOC,index,tf):
    '''
        creation de sousBDOC
    '''
    sousBDOC=sousbdoc.sousBdoc(index,requete)
    #print((sousBDOC))

     

    '''
        la creation d'une matrice tfidf 
    '''
    tfidf_matrice= tfidf.tfidf(sousBDOC,BDOC,tf,index)
    #print(tfidf_matrice)
    
 
    '''
        la creation d'un vecteur de la requete
    '''
    req = requete_vecteur.requete_vecteur(requete,BDOC,index)
    #print(req)
    
    similarite=calculate_similarity(req, tfidf_matrice)
    
    similarities = {}
    sorted_documents = sorted(similarite.items(), key=lambda x: x[1], reverse=True)
    # affichage les 10 top similarités
    for document, similarity in sorted_documents[:10]:
        
        similarities[document]=similarity
        print(f"Document: {document}, Similarity: {similarity}")
    return similarities
