import os
#import Client
def list(m_nom):
    with open("C:/Users/cedri/Desktop/POO/client.txt", "r+") as fil:
        line2=fil.readlines()
        for line in line2:
            start=line.find("*")
            end=line.find("#")# Délimiteur du numero client dans client
            start2=line.find("#")
            end2=line.find("&")# Délimiteur du nom dans client
            if start != -1 and end != -1 and line[start2+1:end2] == m_nom:
                 with open("C:/Users/cedri/Desktop/POO/commande.txt", "r+") as file:
                    line1=file.readlines()
                    for lin in line1:
                        start3=lin.find("*")
                        end3=lin.find("#")# Délimiteur du numero de commande dans commande
                        start4=lin.find("#")
                        end4=lin.find("&") # Délimiteur du numero client dans commande
                        start5=lin.find("&")
                        end5=lin.find("@")# Délimiteur du statut de la commande dans commande
                        if start != -1 and end != -1 and lin[start4+1:end4] == line[start+1:end]:
                            with open("C:/Users/cedri/Desktop/POO/livraison.txt", "r+") as fill:
                                line3=fill.readlines()
                                for li in line3:
                                    start6=li.find("*")
                                    end6=li.find("#") # Délimiteur du numero de commande dans livraison
                                    print(lin[start3+1:end3])
                                    if start != -1 and end != -1 and lin[start5+1:end5] == "en cours" and lin[start3+1:end3] == li[start6+1:end6]:
                                        with open("C:/Users/cedri/Desktop/POO/liste_des_commandes_en_cours.txt", "w+") as fi:
                                            fi.write("".join(["*"+str(line[start2+1:end2]), "#", str(li[start6+1:end6]), "\n"]))
                                        

list("NZIA")
