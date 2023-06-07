import bs4
import os




def readfile(filename):
    with open(filename, 'r', encoding='ISO-8859-1') as file:
        # Load the TEI.2 file
        xml = file.read()
        BDOC = {}
        soup = bs4.BeautifulSoup(xml, "lxml")
        articles = soup.find_all('div', {'type': 'article'})

        for article in articles:
            NumArticle = article.get('id')

            try:
                Title = article.title.get_text()
            except AttributeError:
                Title = " "

            paragraphs = article.find_all('p')
            content = " ".join(paragraph.get_text() for paragraph in paragraphs)

            BDOC[NumArticle] = Title + ' ' + content
    return BDOC

def get_corpus(filename):
    file_path = os.path.join(os.curdir, "AMARYLLIS-98-extrait-OFIL", "OFIL", filename)

    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        # Load the file contents
        xml = file.read()
        # Parse the XML contents with BeautifulSoup
        soup = bs4.BeautifulSoup(xml, "lxml")

    return soup


def get_bdoc_dict(file_content):
    bdoc = dict()

    doc_list = file_content.find_all('div', {'type': 'article'})

    for doc in doc_list:
        doc_id = doc.get('id')
        try:
            doc_title = doc.title.get_text()
        except AttributeError:
            # If the article doesn't have a title element, set it to an empty string
            doc_title = ""

        try:
            doc_text = doc.p.get_text()
        except AttributeError:
            # If the article doesn't have a paragraph element, set it to an empty string
            doc_text = ""

        bdoc[doc_id] = doc_title + ' ' + doc_text

    return bdoc






   







