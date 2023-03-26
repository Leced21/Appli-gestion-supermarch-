#import Commande
#import Client
import os
def recupe(ref):
	with open ("C:/Users/cedri/Desktop/POO/commande.txt", "r+") as file:
		lines=file.readlines()
		for line in lines:
			start=line.find("#")
			end=line.find("&")# délimiteur du numero client dans commande
			start2=line.find("@") # Délimiteur de la référence dans commande
			end2=line.find("!")
			if start != -1 and end != -1 and line[start2+1:end2] == ref:
				with open ("C:/Users/cedri/Desktop/POO/client.txt", "r+") as fil:
					lin=fil.readlines()
					for line2 in lin:
						start3=line2.find("#")# Délimiteur du nom client dans client
						end3=line2.find("&")
						start4=line2.find("*")
						end4=line2.find("#")# delimiteur du numero du client dans client					
						if start != -1 and end != -1 and line[start+1:end] == line2[start4+1:end4]:
							with open ("C:/Users/cedri/Desktop/POO/liste_des_articles_d_un_client.txt", "w+") as fi:
								fi.write("".join(["*", str(line2[start4+1:end4]), "#", str(line2[start3+1:end3]), "&", "\n"]))

recupe("47")
# ajouter le numero et le nom
# ajouter plus de client