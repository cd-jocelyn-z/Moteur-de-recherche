import readfile
import indexation
import interrogation




def get_similarities(requete):
    '''
            similarities un dictionnaire
            {
                document1 : similarity ,
                ......... : .......... ,
                document10: similarity
                }
            
    '''
    
    BDOC = readfile.readfile(".\\AMARYLLIS-98-extrait-OFIL 2\\OFIL\\OD1")
    ## PHASE D'INDEXATION
    index,tf=indexation.indexation(BDOC)
    ## PHASE D'INTERROGATION
    similarities = interrogation.interrogation(requete,BDOC,index,tf)

    return similarities 







        
    

        
     


        
