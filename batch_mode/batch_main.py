import read_file
import numpy as np
import indexation
import interrogation
import tokenization
import batch

'''
        LECTURE DE CORPUS ET PREPARER LE BDOC
'''
print("Reading 'OD1_test.txt'")
file_contents = read_file.get_corpus('OD1_test.txt')
bdoc_dict = read_file.get_bdoc_dict(file_contents)


'''
        PHASE D'INDEXATION
'''
index_dict, doc_term_freq  = indexation.get_index_dict(bdoc_dict)
print()
print("INDEX DICT EX {WORD 1 : {DOC ID : WORD FREQ, DOC ID : WORD FREQ }, {WORD 2 : {DOC ID : WORD FREQ, DOC ID : WORD FREQ }}")
print(index_dict)
print()

'''
        SET-UP [ BATCH ] PHASE D'INTERROGATION 
'''
batch_queries = batch.get_queries("OT1.txt")
expected_docs = batch.get_expected_docs_dict("OT1D1.txt")

print()
print("BATCH QUERY AND ITS CONTENT EX {BATCH QUERY ID : BATCH QUERY}")
print(batch_queries)

print()
print("BATCH QUERY AND LIST OF EXPECTED RESULT EX { BATCH QUERY ID 1 : [DOC_ID_23, DOC_ID_4, DOC_ID_8], BATCH QUERY ID 2 : [DOC_ID_23, DOC_ID_4, DOC_ID_8]}")
print(expected_docs)
print()

'''
        [ BATCH ] PHASE D'INTERROGATION 
'''

batch_interrogation = {}
for batch_q_id, batch_query in batch_queries.items():
    retrieved_docs_dict = interrogation.get_retrieved_docs_dict(index_dict, batch_query)
    batch_interrogation[batch_q_id] = retrieved_docs_dict

print("BATCH INTERROGATION RESULT", batch_interrogation)




