import tokenization as tk

def indexation(BDOC):
    index={} '''Dictionnaire qui a pour clé un mot et pour valeur un autre dictionnaire (dic2). Dic2 a pour clé le doc_id et pour valeur le nombre d'occurences du 
    mot dans ce document'''
    doc_term_freq = {}'''Dictionnaire qui a pour clé un numéro de document (NumArticle) et pour valeur un autre dictionnaire (term_freq_dict). term_freq_dict a pour
    clé un mot et pour valeur le nombre d'occurences de ce mot dans le document NumArticle)'''

    for NumArticle in BDOC.keys():
        dic2={}
        term_freq_dict={}
        for word in tk.tokenization(BDOC[NumArticle]):
            word=word.lower()
            
            if word in term_freq_dict.keys():
                term_freq_dict[word]+=1
            else:
                term_freq_dict[word]=1
                
            if word not in index.keys():
                dic2={NumArticle:0}
                index[word]=dic2
            if word in index.keys():
                if NumArticle in index[word].keys():
                    index[word][NumArticle]+=1
                else:
                    index[word][NumArticle]=1
            
            doc_term_freq[NumArticle]=term_freq_dict
    return index,doc_term_freq
