def get_retrieved_docs_dict(index_dict, user_query):
    segmented_user_query = user_query.lower().split(" ")

    retrieved_docs_dict = {}
    for query_word in segmented_user_query:
        for index_word in index_dict.keys():
            if query_word == index_word:
                retrieved_docs_dict[index_word] = index_dict.get(query_word, {})

    return retrieved_docs_dict
