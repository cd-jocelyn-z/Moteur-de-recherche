import tokenization as tk
import math


'''
        la creation d'une matrice tfidf 
        le retour de cette fonction un dictionnaire de dictionnaire :
        {
            doc1 : {
                        mot1: tf-idf
                        mot2: tf-idf
                        ....
                        motn: tf-idf
                    {
            doc2 :
            doc3 :
            .... :
            docn :
            
            }
'''
def tfidf(sousBDOC,BDOC,tf,index):
    tfidf_matrice = {}
    for document in sousBDOC:
        N= len(BDOC)
        #print("*********************************************************************************************")
        #print("la taille  de BDOC " + str(N))
        tfidf_vecteur = {}
        nombre_motDocument = len(tk.tokenization(BDOC[document]))
        #print("le nombre de mot dans le document", nombre_motDocument)
        for word in tf[document].keys():
            occurence = tf[document][word]
            tf_value = occurence / nombre_motDocument
            #print(f"{document}: ({word}): ({str(occurence)}\{str(nombre_motDocument)})={str(tf_value)}")
            n = len(index[word])
            #print(f"le nombre de document ou le mot ({word}) apparait = {str(n)}")
            idf = math.log10(N/n)
            #print(f"le idf de mot:({word}): ({N}\{n}) = ({str(idf)}))")
            tfidf = tf_value * idf
            #print(f"le tf-idf de :({word}): ({tf_value}*{idf})=({str(tfidf)})")
            tfidf_vecteur[word] = tfidf
            #print(tfidf_vecteur)

        tfidf_matrice[document] =  tfidf_vecteur #normalized_vector
    return tfidf_matrice
