#import Commande
#import Article
import os

def recup(numclient):
	with open ("C:/Users/cedri/Desktop/POO/commande.txt", "r+") as file:
		lines=file.readlines()
		for line in lines:
			start=line.find("#")
			end=line.find("&") # Délimiteur du numclient dans commande
			start2=line.find("@") # Délimiteur de la référence dans commande
			end2=line.find("!")
			if start != -1 and end != -1 and line[start+1:end] == numclient:
				with open ("C:/Users/cedri/Desktop/POO/article.txt", "r+") as fil:
						li=fil.readlines()
						for lin in li:
							start3=lin.find("*")# // Délimiteur de la référence dans article
							end3=lin.find("#")
							start4=lin.find("#") #// Délimiteur du libelé de l'article
							end4=lin.find("&")
							if start != -1 and end != -1 and line[start2+1:end2] == lin[start3+1:end3]:
								with open ("C:/Users/cedri/Desktop/POO/liste_des_articles.txt", "w+") as fi:
									fi.write("".join(["*", str(lin[start3+1:end3]), "#", str(lin[start4+1:end4]), "&","\n"]))

recup("87")