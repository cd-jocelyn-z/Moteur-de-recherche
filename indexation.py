from tokenization import tokenization


def indexation(bdoc_dict):
    index_dict = {}
    doc_term_freq = {}

    for doc_id in bdoc_dict.keys():
        term_freq_dict = {}
        for word in tokenization(bdoc_dict[doc_id]):

            if word in term_freq_dict:
                term_freq_dict[word] += 1
            else:
                term_freq_dict[word] = 1

            if word in index_dict:
                if doc_id in index_dict[word]:
                    index_dict[word][doc_id] += 1
                else:
                    index_dict[word][doc_id] = 1
            else:
                index_dict.setdefault(word, {doc_id: 0})

        doc_term_freq[doc_id] = term_freq_dict

    return index_dict, doc_term_freq