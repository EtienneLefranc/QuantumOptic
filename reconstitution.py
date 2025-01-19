# import igraph as ig
import copy


def produit_chaines(longueurchaines):
    indice_de_la_chaine = 0
    d = {}
    for longueur in longueurchaines:
        i = 0
        while i < longueur:
            avant = i-1
            apres = i+1
            if i == 0:
                d[str(indice_de_la_chaine)+','+str(i)
                  ] = [str(indice_de_la_chaine)+','+str(apres)]
            elif i+1 == longueur:
                d[str(indice_de_la_chaine)+","+str(i)
                  ] = [str(indice_de_la_chaine)+","+str(avant)]
            else:
                d[str(indice_de_la_chaine)+","+str(i)] = [str(indice_de_la_chaine) +
                                                          ","+str(avant), str(indice_de_la_chaine)+","+str(apres)]
            i += 1
        indice_de_la_chaine += 1
    return d


def produit_fusions(fusions):
    resu = []
    for fusion in fusions:
        premier_qubit = str(fusion[0][0])+","+str(fusion[0][1])
        second_qubit = str(fusion[1][0])+","+str(fusion[1][1])
        resu.append([premier_qubit, second_qubit])
    return resu


def reconstitution(dictionnaire_dadjacence_entree, fusions):
    dictionnaire_dadjacence = copy.deepcopy(dictionnaire_dadjacence_entree)
    for i in range(len(fusions)):
        qubit1, qubit2 = fusions[i]
        voisins_de_qubit1, voisins_de_qubit2 = dictionnaire_dadjacence[
            qubit1], dictionnaire_dadjacence[qubit2]
        for voisin in voisins_de_qubit1:
            dictionnaire_dadjacence[voisin] += voisins_de_qubit2
            dictionnaire_dadjacence[voisin].remove(qubit1)
        for voisin in voisins_de_qubit2:
            dictionnaire_dadjacence[voisin] += voisins_de_qubit1
            dictionnaire_dadjacence[voisin].remove(qubit2)
        del dictionnaire_dadjacence[qubit1]
        del dictionnaire_dadjacence[qubit2]
    return dictionnaire_dadjacence


fusions = [["0,0", "0,3"]]
d = {"0,0": ["0,1"], "0,1": ["0,0", "0,2"], "0,2": ["0,1", "0,3"], "0,3": [
    "0,2", "0,4"], "0,4": ["0,3", "0,5"], "0,5": ["0,4", "0,6"], "0,6": ["0,5"]}

chaînesEmile = [0, 5, 0, 8]
fusionsEmile = [((3, 3), (3, 7)), ((3, 5), (3, 0))]


chainesBis = produit_chaines(chaînesEmile)
fusionBis = produit_fusions(fusionsEmile)

dsortie = reconstitution(chainesBis, fusionBis)
print(dsortie)
# graph = ig.Graph.ListDict(dsortie)
# ig.plot(graph)
