import bs4


def readfile(filename):
    with open(filename, 'r') as file:
        # Load the TEI.2 file
        xml = file.read()
        BDOC = {}
        #Collect all the div of type article using BeautifulSoup
        soup=bs4.BeautifulSoup(xml,"lxml")
        articles=soup.find_all('div',{'type':'article'})
        #adding the Article number and its content to a dictionnary
        for article in articles:
            NumArticle=article.get('id')
            try:
                Title=article.title.get_text()
            except AttributeError:
                #print("No title element found in article:", article.get('id'))
                Title=" "

            try:
                Paragraphe=article.p.get_text()
            except AttributeError:
                #print("No title Paragraphe element found in article:", article.get('id'))
                Paragraphe=" "
    
            BDOC[NumArticle]=Title+' '+Paragraphe
    return BDOC





   







