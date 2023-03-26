# Creation de la classe Article et des differentes actions y afferentes
from random import randint
import os
class Article:
    def __init__(self, label="", unit_price="", qqt_stck="", seuil_c=""):
        self.ref=randint(1, 100)
        self.label=label
        self.unit_price=unit_price
        self.qqt_stck=qqt_stck
        self.seuil_c=seuil_c

 # Enregistrement des articles

    def enregistrerarticle(self):
        
        with open("C:/Users/cedri/Desktop/POO/article.txt", "a+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/article.txt"):
                file.write("".join(["*", str(self.ref), "#", str(self.label), "&", str(self.unit_price), "@", str(self.qqt_stck), "!", str(self.seuil_c),"\n"]))
                file.close()
                print("l'article a été crée")
            else:
                print("le fichier n'existe pas")  

# ****** Rechercher un article
                
    def rechercherarticle(self, search_string):
        with open("C:/Users/cedri/Desktop/POO/article.txt", 'r+') as f:
            if os.path.exists("C:/Users/cedri/Desktop/POO/article.txt"):
                for line in f:
                    start = line.find('*')
                    end = line.find('#')
                    if start != -1 and end != -1 and search_string == line[start+1:end]:
                        return 1
        return 0

# **** suppression d'un article
    def supparticle(self, search_string):
        with open("C:/Users/cedri/Desktop/POO/article.txt", "r+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/article.txt"):
                lines=file.readlines()
                #print(lines)
        with open("C:/Users/cedri/Desktop/POO/article_temp.txt", "w+") as fil:
            for line in lines:
                start = line.find('*')
                end = line.find('#')
                if start != -1 and end != -1 and search_string == line[start+1:end]:
                    continue
                fil.writelines(line)
        os.remove("article.txt")
        os.rename("article_temp.txt", "article.txt")





# modification des informations d'un article

    def modifierarticle(self, search_string, nlabel, n_unit_price, nqqt_stck, nseuil_c):
        with open("C:/Users/cedri/Desktop/POO/client.txt", "r+") as file:
            if os.path.exists("C:/Users/cedri/Desktop/POO/article.txt"):
                lines=file.readlines()
                print(lines)
        with open("C:/Users/cedri/Desktop/POO/article_temp.txt", "w+") as fil:
            for line in lines:
                start = line.find('*')
                end = line.find('#')
                if start != -1 and end != -1 and search_string == line[start+1:end]:
                    fil.writelines("*"+str(search_string)+"#"+str(nlabel)+"&"+str(n_unit_price)+"@"+str(nqqt_stck)+"!"+str(nseuil_c))
                    continue
                fil.writelines(line)
        os.remove("article.txt")
        os.rename("article_temp.txt", "article.txt")




article1=Article()
article1.enregistrerarticle()