import numpy


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
# tf = {le:15,je:16,france:100,etre:1}
#document = BDOC[doc]
def tf(index,term):
    tf=index.get(term,"not available")    
    return tf
    
    
    
    
    
    
    
