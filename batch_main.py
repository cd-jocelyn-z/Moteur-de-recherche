from indexation import indexation
from interrogation import interrogation
from read_file import read_corpus
from tfidf import tfidf
import batch

print("\nLecture de la base de données")
bdoc_dict = read_corpus("OD1.txt")
print("Fin de la lecture")

print("\nIndexation en cours")
index_dict, doc_term_freq = indexation(bdoc_dict)
print("Fin de l'indexation")

print("\nCalculs en cours")
documents_tfidf_dict = tfidf(bdoc_dict, doc_term_freq, index_dict)
print("Fin des calculs")

all_similarities = {}

batch_queries = batch.get_queries("OT1.txt")
# print("BATCH QUERY AND ITS CONTENT EX {BATCH QUERY ID : BATCH QUERY}")
# print(batch_queries)

print("\nChargement de la comparaison des requêtes :")
for number, query in batch_queries.items():
    print(f"*** Query number: {number} ***")
    similarities = interrogation(query, bdoc_dict, index_dict, documents_tfidf_dict)
    all_similarities[number] = similarities

# print("BATCH QUERY AND LIST OF EXPECTED RESULT EX { BATCH QUERY ID 1 : [DOC_ID_23, DOC_ID_4, DOC_ID_8], BATCH QUERY ID 2 : [DOC_ID_23, DOC_ID_4, DOC_ID_8]}")
expected_docs = batch.get_expected_docs_dict("OT1D1.txt")
# print(expected_docs)


'''
        [ BATCH ] PHASE D'INTERROGATION 
'''

batch_interrogation = {}
batch_precision = {}
batch_recall = {}
batch_f1_score = {}

for batch_q_id, batch_query in batch_queries.items():
    batch_interrogation[batch_q_id] = all_similarities[batch_q_id]

    retrieved_docs = list(all_similarities[batch_q_id].keys())
    expected_docs_for_query = expected_docs.get(batch_q_id, [])

    common_docs_list = []

    print(f"\nResult for query number: {batch_q_id}")
    print(f"List of Retrieved Documents: {retrieved_docs}")
    print(f"List of Expected Documents: {expected_docs_for_query}")

    for document_num_a in retrieved_docs:
        if document_num_a in expected_docs_for_query:
            common_docs_list.append(document_num_a)

    total_common_docs = len(common_docs_list)
    print(f"Total Documents in common: {total_common_docs}")

    precision = batch.calculate_precision(retrieved_docs, expected_docs_for_query)
    recall = batch.calculate_recall(retrieved_docs, expected_docs_for_query)
    f1_score = batch.calculate_f1_score(precision, recall)

    batch_precision[batch_q_id] = precision
    batch_recall[batch_q_id] = recall
    batch_f1_score[batch_q_id] = f1_score


# print("\nBATCH INTERROGATION RESULT", batch_interrogation)
# print("\nBATCH PRECISION", batch_precision)
# print("\nBATCH RECALL", batch_recall)

print(f"\nBATCH F1 SCORE {batch_f1_score}")
