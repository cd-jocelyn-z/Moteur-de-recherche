import re
import os
from interrogation import interrogation


#Retourne le dictionnaire contenant {num de requête:[les documents]} OU les documents d'un q_id spécifié
def extract_dico_docs_attendus(filename,q_id=None):
    
    dico_docs_attendus = {} 
    filepath = os.path.join(os.curdir, "AMARYLLIS-98-extrait-OFIL", "OFIL", filename)
    
    with open(filepath, 'r') as file:
        document = file.read()
        pattern = r"<record><qid>(\d+)</qid>(.*?)<\/record>"
        matches = re.findall(pattern, document, flags=re.DOTALL)

        for match in matches:
            qid = match[0]
            
            doc_nos = re.findall(r"<docno>(\d+)<\/docno>", match[1])
            if qid == q_id:
                return doc_nos
            dico_docs_attendus[qid] = doc_nos

    return dico_docs_attendus




def get_query(q_id,filename): #Récupère le contenu d'une requête de OT1
    
    filepath = os.path.join(os.curdir, "AMARYLLIS-98-extrait-OFIL", "OFIL", filename)
    
    with open(filepath, 'r') as file:
        document = file.read()

        pattern = r"<record>\s*<num>(\d+)<\/num>(.*?)<\/record>"
        matches = re.findall(pattern, document, flags=re.DOTALL)

        for match in matches:
            num = match[0]
            if num == q_id:
                query = re.search(r"<que>(.*?)<\/que>", match[1])
                if query:
                    return query.group(1).strip()

    return None




def evaluation_G(index,tf,nlp): #Fournit une évaluation générale du moteur de recherche 
    
    Precision_generale = 0.0 
    Recall_general = 0.0 
    Precision_min = 1.0 
    Precision_max = 0.0 
    Recall_min = 1.0 
    Recall_max = 0.0 
    q_id_pmin = 0 #numéro de la requête pour laquelle la précision est minimale
    q_id_pmax = 0 #numéro de la requête pour laquelle la précision est maximale
    q_id_rmin = 0 #numéro de la requête pour laquelle le rappel est minimal
    q_id_rmax = 0 #numéro de la requête pour laquelle le rappel est maximal
    Somme_precision = 0.0 
    Somme_recall = 0.0 
    F1_score = 0.0
    
    dico_docs_attendus = {}
    dico_docs_attendus = extract_dico_docs_attendus("OT1D1") #On récupère le dictionnaire {num_req:[docs attendus]}
    
    for q_id in dico_docs_attendus.keys(): #Pour chaque numéro de requête
        
        Docs_matchés = 0 
        Precision = 0.0
        Recall = 0.0
        
        req = get_query(q_id,"OT1") #On récupère le contenu de la requête
        dico_docs_renvoyés = interrogation(req,index,tf,nlp) #On "l'entre" dans notre moteur de recherche
        
        for doc in dico_docs_attendus[q_id]: #Pour chaque document attendu (de la requête considérée dans le premier for)
            if doc in dico_docs_renvoyés.keys(): #Si le document est aussi présent parmi les document renvoyés par le moteur de recherche
                Docs_matchés += 1 #On ajoute un match
        
        Precision = Docs_matchés/len(dico_docs_renvoyés) #Calcul de la précision pour la requête considérée 
        Recall = Docs_matchés/len(dico_docs_attendus[q_id]) #Calcul du rappel pour la requête considérée 
            
        
        """Calcul des précisions min et max et des rappels min et max"""
        
        if Precision<Precision_min: #Dans le cas où on trouve une nouvelle précision minimale
            Precision_min = Precision
            q_id_pmin = q_id
        if Precision>Precision_max: #Dans le cas où on trouve une nouvelle précision maximale
            Precision_max = Precision
            q_id_pmax = q_id
        if Recall<Recall_min: #Dans le cas où on trouve un nouveau rappel minimal
            Recall_min = Recall
            q_id_rmin = q_id
        if Recall>Recall_max: #Dans le cas où on trouve un nouveau rappel maximal
            Recall_max = Recall
            q_id_rmax = q_id
                
                
        Somme_precision += Precision
        Somme_recall += Recall
    
    Precision_generale = Somme_precision/len(dico_docs_attendus) #Précision globale (moyenne des précisions pour chaque requête)
    Recall_general = Somme_recall/len(dico_docs_attendus) #Rappel global (moyenne des rappels pour chaque requête)
    F1_score = 2 * (Precision_generale * Recall_general) / (Precision_generale + Recall_general)
        
    print(f"Précision générale : {Precision_generale}\nRappel général : {Recall_general}")
    print(f"Le score F1 est de : {F1_score}")
    print(f"La précision la plus élevée est de : {Precision_max} (requête numéro {q_id_pmax})")
    print(f"La précision la plus faible est de : {Precision_min} (requête numéro {q_id_pmin})")
    print(f"Le rappel le plus élevé est de : {Recall_max} (requête numéro {q_id_rmax})")
    print(f"Le rappel le plus faible est de : {Recall_min} (requête numéro {q_id_rmin})")





def evaluation_micro(index,tf,nlp): #Fournit une évaluation pour une requête précise 
    
    Réponse2 = input("Entrez le numéro de la requête (entre 1 et 11 ou entre 16 et 30)\n").lower()
    Precision_m = 0.0
    Recall_m = 0.0
    
    if (int(Réponse2)>11 and int(Réponse2)<16) or int(Réponse2)>30: #On vérifie que le numéro de la requête est valide
        print("La requête n'existe pas!")
    
    else:
        Docs_matchés = 0
        Docs_attendus = []
        Docs_attendus = extract_dico_docs_attendus("OT1D1",Réponse2) #On récupère les documents attendus pour le numéro de requête contenu dans Réponse 2
        req = get_query(Réponse2,"OT1") #On récupère le contenu de la requête 
        dico_docs_renvoyés = interrogation(req,index,tf,nlp) #On "l'entre" dans notre moteur de recherche
        
        for doc in Docs_attendus: #Pour chaque document attendu 
            if doc in dico_docs_renvoyés.keys(): #Si le document est aussi présent parmi les document renvoyés par le moteur de recherche
                Docs_matchés += 1 #On ajout un match 
        
        Precision_m = Docs_matchés/len(dico_docs_renvoyés) #Calcul de la micro précision (pour une requête)
        Recall_m = Docs_matchés/len(Docs_attendus) #Calcul du micro rappel (pour une requête)
        
        print(f"Pour la requête {Réponse2}:\n Précision : {Precision_m}\n Rappel : {Recall_m}")