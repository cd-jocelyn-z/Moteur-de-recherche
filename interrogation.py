from request_process import request_processing
from similarities import calculate_similarity


def interrogation(query, bdoc_dict, index_dict, documents_tfidf_dict):
    request_tfidf_dict = request_processing(query, bdoc_dict, index_dict)

    similarities = calculate_similarity(request_tfidf_dict, documents_tfidf_dict)

    sorted_similarities = {}
    sorted_documents = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    for document, similarity in sorted_documents[:10]:
        sorted_similarities[document] = similarity

    return sorted_similarities