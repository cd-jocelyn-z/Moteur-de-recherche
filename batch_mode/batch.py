import os.path
import re


def get_query_file(filename):
    file_path = os.path.join(os.curdir, "AMARYLLIS-98-extrait-OFIL", "OFIL", filename)

    with open(file_path, "r", encoding="ISO-8859-1") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]


def get_queries(filename):
    queries_dict = dict()
    lines = get_query_file(filename)
    record_contents = "".join(lines)

    pattern_query_id = r"<num>(\d{1,})<\/num>"
    query_ids = re.findall(pattern_query_id, record_contents, flags=re.DOTALL)

    pattern_query = r"<que>(.*?)<\/que>"
    queries = re.findall(pattern_query, record_contents, flags=re.DOTALL)

    for q_id in query_ids:
        for query in queries:
            if q_id not in queries_dict:
                queries_dict[q_id] = query

    return queries_dict


# print(get_queries("OT1.txt"))


# Process file OT1D1
def get_expected_docs_file(filename):
    file_path = os.path.join(os.curdir, "AMARYLLIS-98-extrait-OFIL", "OFIL", filename)

    with open(file_path, "r") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]


def get_expected_docs_dict(filename):
    expected_docs_dict = dict()
    lines = get_expected_docs_file(filename)
    record_contents = "".join(lines)

    pattern_query_id = r"<qid>(\d{1,})<\/qid>"
    query_ids = re.findall(pattern_query_id, record_contents, flags=re.DOTALL)

    pattern_doc_no = r"<docno>(\d{1,})<\/docno>"
    doc_nos = re.findall(pattern_doc_no, record_contents, flags=re.DOTALL)

    for q_id in query_ids:
        pattern = r"<qid>" + q_id + r"<\/qid>(.*?)<\/record>"
        result = re.findall(pattern, record_contents, flags=re.DOTALL)[0]
        doc_nos_for_qid = re.findall(pattern_doc_no, result, flags=re.DOTALL)

        expected_docs_dict[q_id] = doc_nos_for_qid

    return expected_docs_dict

# print(get_expected_docs_dict("OT1D1.txt"))


def calculate_precision(retrieved_docs, expected_docs):
    retrieved_set = set(retrieved_docs)
    expected_set = set(expected_docs)
    relevant_set = retrieved_set.intersection(expected_set)
    precision = len(relevant_set) / len(retrieved_set) if len(retrieved_set) > 0 else 0.0
    return precision


def calculate_recall(retrieved_docs, expected_docs):
    retrieved_set = set(retrieved_docs)
    expected_set = set(expected_docs)
    relevant_set = retrieved_set.intersection(expected_set)
    recall = len(relevant_set) / len(expected_set) if len(expected_set) > 0 else 0.0
    return recall


def calculate_f1_score(precision, recall):
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    return f1_score