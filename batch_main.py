import readfile
import indexation
import interrogation
import tokenization
import batch





'''
        LECTURE DE CORPUS ET PREPARER LE BDOC
'''

print("Reading database.....")

BDOC = readfile.readfile(".\\AMARYLLIS-98-extrait-OFIL 2\\OFIL\\OD1")

print("end of reading !")



'''
        PHASE D'INDEXATION
        
        INDEX DICT EX {
                       WORD 1 : {DOC ID : WORD FREQ, DOC ID : WORD FREQ },
                       WORD 2 : {DOC ID : WORD FREQ, DOC ID : WORD FREQ }
                       }
        
'''
index,tf=indexation.indexation(BDOC)


'''
        SET-UP [ BATCH ] PHASE D'INTERROGATION

        
        all_similarities = { numéro requete 1 : { doc1 : similarity
                                                doc2 : similarity
                                                ...  : ..........
                                                doc10: similarity
                             numéro requete 2 : {documents : similarities
                                                     }
                                        }       
'''
all_similarities={}

batch_queries = batch.get_queries("OT1.txt")
print("BATCH QUERY AND ITS CONTENT EX {BATCH QUERY ID : BATCH QUERY}")
print(batch_queries)

for number,query in batch_queries.items():
    print(f"***query number #{number}:****")
    similarities = interrogation.interrogation(query,BDOC,index,tf) #calculate the similarities of one query using the interrogation function
    all_similarities[number]=similarities

print(all_similarities)


print("BATCH QUERY AND LIST OF EXPECTED RESULT EX { BATCH QUERY ID 1 : [DOC_ID_23, DOC_ID_4, DOC_ID_8], BATCH QUERY ID 2 : [DOC_ID_23, DOC_ID_4, DOC_ID_8]}")
expected_docs = batch.get_expected_docs_dict("OT1D1.txt")
print(expected_docs)



'''
        [ BATCH ] PHASE D'INTERROGATION 
'''

batch_interrogation = {}
batch_precision = {}
batch_recall = {}
batch_f1_score = {}

for batch_q_id, batch_query in batch_queries.items():
    retrieved_docs_dict = interrogation.get_retrieved_docs_dict(index_dict, batch_query)
    batch_interrogation[batch_q_id] = retrieved_docs_dict

    retrieved_docs = list(retrieved_docs_dict.keys())
    expected_docs_for_query = expected_docs.get(batch_q_id, [])

    precision = batch.calculate_precision(retrieved_docs, expected_docs_for_query)
    recall = batch.calculate_recall(retrieved_docs, expected_docs_for_query)
    f1_score = batch.calculate_f1_score(precision, recall)

    batch_precision[batch_q_id] = precision
    batch_recall[batch_q_id] = recall
    batch_f1_score[batch_q_id] = f1_score

print("\nBATCH INTERROGATION RESULT", batch_interrogation)
print("\nBATCH PRECISION", batch_precision)
print("\nBATCH RECALL", batch_recall)
print("\nBATCH F1 SCORE", batch_f1_score)




