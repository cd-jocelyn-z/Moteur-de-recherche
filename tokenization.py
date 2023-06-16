import re


def tokenization(content): #Prend en entrée un contenu et renvoie une liste contenant les tokens

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





