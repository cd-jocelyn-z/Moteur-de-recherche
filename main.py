from indexation import indexation
from interrogation import interrogation
from read_file import read_corpus
from tfidf import tfidf

print("Lecture de la base de données")
bdoc_dict = read_corpus("OD1.txt")
print("Fin de la lecture")

print("Indexation en cours")
index_dict, doc_term_freq = indexation(bdoc_dict)
print("Fin de l'indexation")

print("Calculs en cours")
documents_tfidf_dict = tfidf(bdoc_dict, doc_term_freq, index_dict)
print("Fin des calculs")

# while True:
# Pourquoi et comment avoir divisé la Tchécoslovaquie et quelles ont été les répercussions économiques et sociales ?
# query = input("Entrez votre requête")
query = "Pourquoi et comment avoir divisé la Tchécoslovaquie et quelles ont été les répercussions économiques et sociales ?"

similarities = interrogation(query, bdoc_dict, index_dict, documents_tfidf_dict)

print(similarities)