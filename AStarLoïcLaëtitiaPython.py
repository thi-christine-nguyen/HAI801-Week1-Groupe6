
liste_sommet  = ['A','B','C','D','E','F','G','H'] # Liste indexée des sommets
poids_sommet = [9,3,5,6,8,4,2,0]
liste_arretes  = [['A','B'],['A','C'],['A','D'],['B','E'],['D','C'],['D','F'],['C','G'],['F','G'],['F','E'],['G','H'],['E','H']] # Liste indexée des sommets
liste_poids_arrete = [2,10,3,8,2,4,2,5,5,1,10]

def evaluer(indice):
    return distance_relle_parcouru[indice] + poids_sommet[indice]

def trier_closed_list():
    for i in range(len(closed_list)):
        for j in range(len(closed_list)):
            if i < j:
                if evaluer(closed_list[i]) > evaluer(closed_list[j]):
                    temp = closed_list[i]
                    closed_list[i] = closed_list[j]
                    closed_list[j] = temp


def recupererPoidsArrete(arrete_construite):
    if arrete_construite not in liste_arretes:
        temp = arrete_construite[0]
        arrete_construite[0] = arrete_construite[1]
        arrete_construite[1] = temp
    return liste_poids_arrete[liste_arretes.index(arrete_construite)]



sommet_depart = 0
open_list = [0] # Initialement que A
closed_list = []
sommet_fin = len(liste_sommet)-1 # Donc H

distance_relle_parcouru = [0,0,0,0,0,0,0,0] # Correspond à la distance réelle pour accéder à open_list[i] 


while len(open_list) != 0:
    u = open_list.pop(0) # On défile
    if u == sommet_fin:
        print("Chemin trouvé")
        break
    
    # Construire la liste des voisins
    nom_sommet = liste_sommet[u]
    liste_voisin = []
    for i in range(len(liste_arretes)):
        if liste_arretes[i][0] == nom_sommet:
            liste_voisin.append(liste_arretes[i][1])

    # Convertir les noms en indice
    for i in range(len(liste_voisin)):
        liste_voisin[i] = liste_sommet.index(liste_voisin[i])
    
    for i in range(len(liste_voisin)):
        if (liste_voisin[i] not in closed_list) or (liste_voisin[i] in open_list and evaluer(liste_voisin[i]) < evaluer(u) ):
            arrete_construite = [liste_sommet[u],liste_sommet[liste_voisin[i]]]
            distance_relle_parcouru[liste_voisin[i]] = distance_relle_parcouru[u] + recupererPoidsArrete(arrete_construite) 
            open_list.append(liste_voisin[i])
    if u not in closed_list:
        closed_list.append(u)
        trier_closed_list()

print(closed_list)
