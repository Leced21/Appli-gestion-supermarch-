# Creation de la classe commande et des differentes actions y afferentes
from random import randint
import Client
import os
class Commande:
    def __init__(self, n_client="", state="en cours", ref_order="", qqt_order=""):
        self.order=randint(1, 100)
        self.m_numclient=n_client
        self.state=state
        self.ref_order=ref_order
        self.qqt_order=qqt_order

 # Enregistrement des commandes

    def enregistrercommande(self):
        
        with open("C:/Users/cedri/Desktop/POO/commande.txt", "a+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/commande.txt"):
                file.write("".join(["*", str(self.order), "#", str(self.m_numclient), "&",str(self.state), "@",str(self.ref_order),  "!",str(self.qqt_order), "\n"]))
                file.close()
                print("la commande a été crée")
            else:
                print("le fichier n'existe pas")  

# ****** Rechercher un commande
                
    def recherchercommande(self, search_string):
        with open("C:/Users/cedri/Desktop/POO/commande.txt", 'r+') as f:
            if os.path.exists("C:/Users/cedri/Desktop/POO/commande.txt"):
                for line in f:
                    start = line.find('*')
                    end = line.find('#')
                    if start != -1 and end != -1 and search_string == line[start+1:end]:
                        return 1
        return 0

# **** suppression d'un coammande
    def suppcommande(self, search_string):
        with open("C:/Users/cedri/Desktop/POO/commande.txt", "r+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/commande.txt"):
                lines=file.readlines()
                #print(lines)
        with open("C:/Users/cedri/Desktop/POO/commande_temp.txt", "w+") as fil:
            for line in lines:
                start = line.find('*')
                end = line.find('#')
                if start != -1 and end != -1 and search_string == line[start+1:end]:
                    continue
                fil.writelines(line)
        os.remove("commande.txt")
        os.rename("commande_temp.txt", "commande.txt")





# modification des informations d'un commande

    def modifierclient(self, search_string, nber_client, nstate, nref, nqqt):
        with open("C:/Users/cedri/Desktop/POO/commande.txt", "r+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/commande.txt"):
                lines=file.readlines()
                print(lines)
        with open("C:/Users/cedri/Desktop/POO/commande_temp.txt", "w+") as fil:
            for line in lines:
                start = line.find('*')
                end = line.find('#')
                if start != -1 and end != -1 and search_string == line[start+1:end]:
                    fil.writelines("*"+str(search_string)+"#"+str(nber_client)+"&"+str(nstate)+"@"+str(nref)+"!"+str(nqqt))
                    continue
                fil.writelines(line)
        os.remove("commande.txt")
        os.rename("commande_temp.txt", "commande.txt")
