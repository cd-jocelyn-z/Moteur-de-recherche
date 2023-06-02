import readfile
import numpy as np
import indexation
import interrogation
import tokenization as tk
import tf


print("reading the content of the files.....")
BDOC = readfile.readfile(".\\AMARYLLIS-98-extrait-OFIL 2\\OFIL\\OD1")
print("end of reading")

## PHASE D'INDEXATION
index=indexation.indexation(BDOC)



## PHASE D'INTERROGATION
requete="italie france"
result=interrogation.interrogation(index,requete)
#print(result)



france_keys = set(result["france"].keys())
#print(france_keys)
italie_keys = set(result["italie"].keys())
#print(italie_keys)
common_keys = france_keys.intersection(italie_keys)
common_keys=list(common_keys)

#print(common_keys)


t=set()
for ID in common_keys:
        content=BDOC[ID]
        tokens=set(tk.tokenization(content))
        t.update(tokens)


# le t c'est tous les mots non repétés dans les documents en commun

#print(t)

'''
        le calcule de tf 
'''
terms=list(t)
num_docs = len(common_keys)
num_terms =len(terms)
tf = np.zeros((num_docs, num_terms))
# matrice de frequence [doc,term] = frequence
for i,ID in enumerate(common_keys):
        b=[]
        content= BDOC[ID]
        tokens=tk.tokenization(content)
        for term in terms:
            if term in tokens:
                frequency=index[term][ID]
                b.append(frequency)     
            else:
                b.append(0)
        vecteur=np.array(b)
        tf[i,:] = vecteur

#print(tf)



        #calculer le idf

print(terms[0])
print(terms[1])
print(terms[2])
tf_transpose =tf.transpose()
# Get the size of the rows
row_size = tf_transpose.shape[0]
print(row_size)
idf = np.zeros((row_size,1))


# Count the number of non-zero entries in the i-th column of M
i = 1 # The word we are interested in
for i in range(row_size):
        num_docs = np.count_nonzero(tf_transpose[i, :])
        idf[i,:]=num_docs
        #print(f"The word '{i}' appears in {num_docs} documents.")
print(idf)


