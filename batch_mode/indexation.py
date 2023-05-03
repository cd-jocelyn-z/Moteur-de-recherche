import re


def get_index_dict(bdoc_dict):
    index_dict = {}

    for doc_id, doc_text in bdoc_dict.items():
        words = re.split(r'[,()_\".?\s\']+', doc_text.lower())
        doc_freq_dict = {}

        for word in words:
            if word in index_dict:
                if doc_id in index_dict[word]:
                    index_dict[word][doc_id] += 1
                else:
                    index_dict[word][doc_id] = 1
            else:
                doc_freq_dict = {doc_id: 1}
                index_dict[word] = doc_freq_dict

    return index_dict