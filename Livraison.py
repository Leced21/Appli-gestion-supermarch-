# Creation de la classe livraison et des differentes actions y afferentes
from random import randint
import Commande
import os
class Livraison:
    def __init__(self, n_order="", qqt="", n_client=""):
        self.order=n_order
        self.qqt=qqt
        self.m_numclient=n_client

 # Enregistrement des livraisons

    def enregistrerlivraison(self):
        
        with open("C:/Users/cedri/Desktop/POO/livraison.txt", "a+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/livraison.txt"):
                file.write("".join(["*", str(self.order), "#", str(self.qqt), "&", str(self.m_numclient),"\n"]))
                file.close()
                print("la livraison a été crée")
            else:
                print("le fichier n'existe pas")  

# ****** Rechercher un livraison
                
    def rechercherclient(self, search_string, file_path):
        with open(file_path, 'r+') as f:
            if os.path.exists("C:/Users/cedri/Desktop/POO/livraison.txt"):
                for line in f:
                    start = line.find('*')
                    end = line.find('#')
                    if start != -1 and end != -1 and search_string == line[start+1:end]:
                        return 1
        return 0

# **** suppression d'un livraison
    def suppclient(self, search_string):
        with open("C:/Users/cedri/Desktop/POO/livraison.txt", "r+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/livraison.txt"):
                lines=file.readlines()
                #print(lines)
        with open("C:/Users/cedri/Desktop/POO/livraison_temp.txt", "w+") as fil:
            for line in lines:
                start = line.find('*')
                end = line.find('#')
                if start != -1 and end != -1 and search_string == line[start+1:end]:
                    continue
                fil.writelines(line)
        os.remove("livraison.txt")
        os.rename("livraison_temp.txt", "livraison.txt")





# modification des informations d'un livraison

    def modifierclient(self, search_string, number, qqt, n_client):
        with open("C:/Users/cedri/Desktop/POO/livraison.txt", "r+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/livraison.txt"):
                lines=file.readlines()
                print(lines)
        with open("C:/Users/cedri/Desktop/POO/livraison_temp.txt", "w+") as fil:
            for line in lines:
                start = line.find('*')
                end = line.find('#')
                if start != -1 and end != -1 and search_string == line[start+1:end]:
                    fil.writelines("*"+str(search_string)+"#"+str(number)+"&"+str(qqt)+"@"+str(n_client))
                    continue
                fil.writelines(line)
        os.remove("livraison.txt")
        os.rename("livraison_temp.txt", "livraison.txt")
