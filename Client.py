# Creation de la classe client et des differentes actions y afferentes
from random import randint
import os
class Client:
    def __init__(self, nom="", prenom="", date_naissance="", genre="M"):
        self.m_numclient=randint(1, 100)
        self.m_nom=nom
        self.m_prenom=prenom
        self.m_date_naissance=date_naissance
        self.m_genre=genre

 # Enregistrement des clients

    def enregistrerclient(self):
        
        with open("C:/Users/cedri/Desktop/POO/client.txt", "a+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/client.txt"):
                file.write("".join(["*", str(self.m_numclient), "#", str(self.m_nom), "&", str(self.m_prenom), "@", str(self.m_date_naissance), "!", str(self.m_genre),"\n"]))
                file.close()
                print("le client a été crée")
            else:
                print("le fichier n'existe pas")  

# ****** Rechercher un client
                
    def rechercherclient(self, search_string):
        with open("C:/Users/cedri/Desktop/POO/client.txt", 'r+') as f:
            if os.path.exists("C:/Users/cedri/Desktop/POO/client.txt"):
                for line in f:
                    start = line.find('*')
                    end = line.find('#')
                    if start != -1 and end != -1 and search_string == line[start+1:end]:
                        return 1
                    
        return 0

# **** suppression d'un client
    def suppclient(self, search_string):
        with open("C:/Users/cedri/Desktop/POO/client.txt", "r+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/client.txt"):
                lines=file.readlines()
                #print(lines)
        with open("C:/Users/cedri/Desktop/POO/client_temp.txt", "w+") as fil:
            for line in lines:
                start = line.find('*')
                end = line.find('#')
                if start != -1 and end != -1 and search_string == line[start+1:end]:
                    continue
                fil.writelines(line)
        os.remove("client.txt")
        os.rename("client_temp.txt", "client.txt")



# modification des informations d'un client

    def modifierclient(self, search_string, nom, prenom, date, sexe):
        with open("C:/Users/cedri/Desktop/POO/client.txt", "r+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/client.txt"):
                lines=file.readlines()
        with open("C:/Users/cedri/Desktop/POO/client_temp.txt", "w+") as fil:
            for line in lines:
                start = line.find('*')
                end = line.find('#')
                if start != -1 and end != -1 and search_string == line[start+1:end]:
                    fil.writelines("*"+str(search_string)+"#"+str(nom)+"&"+str(prenom)+"@"+str(date)+"!"+str(sexe))
                    continue
                fil.writelines(line)
        os.remove("client.txt")
        os.rename("client_temp.txt", "client.txt")
