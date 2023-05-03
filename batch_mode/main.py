import os.path
import re


# Process : OT1
def get_query_file(filename):
    path_to_txt_file = os.path.join(os.curdir, filename)

    with open(path_to_txt_file, "r") as file:
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


print(get_queries("OT1.txt"))


# Process : OT1D1
def get_expected_docs_file(filename):
    path_to_txt_file = os.path.join(os.curdir, filename)

    with open(path_to_txt_file, "r") as file:
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


print(get_expected_docs_dict("OT1D1.txt"))