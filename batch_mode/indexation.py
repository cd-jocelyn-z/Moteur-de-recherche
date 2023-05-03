import tokenization


def get_index_dict(bdoc_dict):
    index_dict = {}
    doc_term_freq = {}

    for doc_id, doc_text in bdoc_dict.items():
        term_freq_dict = {}
        for word in tokenization.get_tokens(doc_text):
            word = word.lower()

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
                doc_freq_dict = {doc_id: 1}
                index_dict[word] = doc_freq_dict

        doc_term_freq[doc_id] = term_freq_dict

    return index_dict, doc_term_freq
