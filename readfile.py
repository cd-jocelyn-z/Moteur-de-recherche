from bs4 import BeautifulSoup

'''
La fonction readfile prend en entrée le chemin vers le fichier xml (OD1) et renvoie un dictionnaire contenant le numéro d'article
et son contenu. BDOC = {article_id:content}
'''


def readfile(filepath): 
    with open(filepath, 'r') as file:
        # Load the TEI.2 file
        xml = file.read()
        BDOC = {}
        soup = BeautifulSoup(xml, "lxml")
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






   







