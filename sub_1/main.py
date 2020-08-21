# this version is under development and could possibly be affected by bugs or other

# importation des modules complementaires 

from modules import *

# definition des variables globales 

global hosta,hostb,temp
      
hosta,hostb,temp= intro()

# utilisation des processus en parralele

t1=threading.Thread(target=serveur)
t2=threading.Thread(target=client)

t1.start()
t2.start()

while 1:
    
    t1.join()
    t2.join()
