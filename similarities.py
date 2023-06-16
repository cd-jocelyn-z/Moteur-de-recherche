import math


def calculate_similarity(request_tfidf_dict, documents_tfidf_dict):
    similarity_scores = {}

    for doc_id, doc in documents_tfidf_dict.items():
        request_vector = list()
        document_vector = list()

        tokens = []
        for key in request_tfidf_dict.keys():
            tokens.append(key)

        for key in doc.keys():
            if key not in tokens:
                tokens.append(key)

        for token in tokens:
            request_vector.append(request_tfidf_dict.get(token, 0))
            document_vector.append(doc.get(token, 0))

        # Calculate dot product
        dot_product = sum(req_value * doc_value for req_value, doc_value in zip(request_vector, document_vector))

        # Calculate Euclidean norm
        request_norm = math.sqrt(sum(value ** 2 for value in request_vector))
        documents_norm = math.sqrt(sum(value ** 2 for value in document_vector))

        # Calculate cosine similarity
        similarity_scores[doc_id] = dot_product / (request_norm * documents_norm)

    return similarity_scores