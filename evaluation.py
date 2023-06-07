import readfile
import indexation
import interrogation
import os



def get_similarities(requete):
    '''
            similarities un dictionnaire
            {
                document1 : similarity ,
                ......... : .......... ,
                document10: similarity
                }
            
    '''
    file_path = os.path.join(os.curdir, "AMARYLLIS-98-extrait-OFIL 2", "OFIL", "OD1")
    BDOC = readfile.readfile(file_path)
    ## PHASE D'INDEXATION
    index,tf=indexation.indexation(BDOC)
    ## PHASE D'INTERROGATION
    similarities = interrogation.interrogation(requete,BDOC,index,tf)

    return similarities 






        
    

        
     


        
