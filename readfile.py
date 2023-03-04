import bs4

# Load the TEI.2 file
def readfile(filename):
    with open(filename, 'r') as file:
        xml = file.read()
  
    return xml
BDOC = {}
xml = readfile(".\\AMARYLLIS-98-extrait-OFIL 2\\OFIL\\OD1")
soup=bs4.BeautifulSoup(xml,"lxml")
articles=soup.find_all('div',{'type':'article'})
print(len(articles))
for article in articles:
    NumArticle=article.get('id')
    try:
        Title=article.title.get_text()
    except AttributeError:
        print("No title element found in article:", article.get('id'))
        Title=" "

    try:
        Paragraphe=article.p.get_text()
    except AttributeError:
        print("No title Paragraphe element found in article:", article.get('id'))
        Paragraphe=" "
    
    BDOC[NumArticle]=Title+' '+Paragraphe

print(len(BDOC))
   







