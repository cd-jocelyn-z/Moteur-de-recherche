import re
import unicodedata

def tokenization(content): #Prend en entrée un contenu et renvoie une liste contenant les tokens

<<<<<<< HEAD
    separateurs = r"\(|\)|\[|\]|\{|\}|<|>|«|»|\"|\'|:|\.\.\.|,|\s|\b|\?|!|\."
    tokens = [mot for mot in re.split(rf"(?:{separateurs})+", content) if mot]
    lowercase_tokens = [token.lower() for token in tokens]

    return lowercase_tokens

def delete_stop_words(query_tokens,stop_words): #Suppression des stop words de la requête
    requete = []
    for token in query_tokens:
        if token not in stop_words:
            requete.append(token)
    return requete




=======
def tokenization(content):
    lowercase_content = content.lower()
    normalized_text = unicodedata.normalize('NFD', lowercase_content)
    diacritic_pattern = re.compile(r'[\u0300-\u036f]')
    text_without_diacritics = diacritic_pattern.sub('', normalized_text)
    tokens = re.split(r'[,()_\"\-:.?\s\']+', text_without_diacritics)
>>>>>>> 2b8df62f9ebb07f58cc2ae16cbcacee26df68861

    return tokens