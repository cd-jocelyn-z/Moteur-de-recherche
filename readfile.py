import bs4





def readfile(filename):
    with open(filename, 'r') as file:
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






   







