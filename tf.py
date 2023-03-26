import numpy as np
import tokenization


'''
TF = (number of times the term appears in the document)
/ (total number of terms in the document
'''

'''
inputs: 
BDOC
{id: content}
index
{  le:{doc1:1,doc2:3,doc3:14,doc5:6},
   je:{doc1:4,doc2:5,doc10:9}
    }
'''

def tf(index,BDOC):
    tf=np.array([])
    
    terms = index.keys()
    for ID in BDOC.keys():
        content= BDOC[ID]
        tokens=tokenization(content)  
        for term in terms:
            if term in tokens:
                frequency=index[term][ID]
                b.append(frequency)                
            else:
                b.append(0)
        vecteur=np.array(b)
        tf=np.vstack(tf,vecteur)
    return tf
                
            
    
    
    
    
    
    
    
