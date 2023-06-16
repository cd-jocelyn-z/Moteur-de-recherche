import os
import bs4


def read_corpus(file_name):
    file_path = os.path.join(os.curdir, "AMARYLLIS-98-extrait-OFIL", "OFIL", file_name)

    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        # Load the file contents
        xml = file.read()
        # Parse the XML contents with BeautifulSoup
        content = bs4.BeautifulSoup(xml, "lxml")

        bdoc_dict = get_bdoc_dict(content)

    return bdoc_dict


def get_bdoc_dict(file_content):
    bdoc_dict = dict()

    doc_list = file_content.find_all('div', {'type': 'article'})

    for doc in doc_list:
        doc_id = doc.get('id')
        try:
            doc_title = doc.title.get_text()
        except AttributeError:
            # If the article doesn't have a title element, set it to an empty string
            doc_title = ""

        try:
            doc_text = ""

            for text in doc.find_all('p'):
                doc_text += text.get_text() + " "
        except AttributeError:
            # If the article doesn't have a paragraph element, set it to an empty string
            doc_text = ""

        bdoc_dict[doc_id] = doc_title + ' ' + doc_text

    return bdoc_dict