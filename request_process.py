from tokenization import tokenization

import math


def request_processing(query, bdoc_dict, index_dict):
    total_documents = len(bdoc_dict)
    request_tfidf_dict = {}
    query_tokenized = tokenization(query)
    total_tokens_in_query = len(query_tokenized)

    for token in query_tokenized:
        if token in index_dict.keys():
            term_occurrence = query_tokenized.count(token)
            term_frequency = term_occurrence / total_tokens_in_query
            idf = math.log10(total_documents / len(index_dict[token]))
            tfidf = term_frequency * idf
            request_tfidf_dict[token] = tfidf

    return request_tfidf_dict