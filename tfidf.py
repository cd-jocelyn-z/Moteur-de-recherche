import math

from tokenization import tokenization


def tfidf(bdoc_dict, doc_term_freq, index_dict):
    documents_tfidf_dict = {}

    for document_id in bdoc_dict:
        total_documents = len(bdoc_dict)
        tfidf_inner_dict = {}
        total_tokens_in_document = len(tokenization(bdoc_dict[document_id]))

        for token in doc_term_freq[document_id].keys():
            token_occurrence = doc_term_freq[document_id][token]
            term_frequency = token_occurrence / total_tokens_in_document
            total_documents_containing_the_word = len(index_dict[token])
            idf = math.log10(total_documents / total_documents_containing_the_word)
            tfidf = term_frequency * idf
            tfidf_inner_dict[token] = tfidf

        # normalized_vector
        documents_tfidf_dict[document_id] = tfidf_inner_dict

    return documents_tfidf_dict