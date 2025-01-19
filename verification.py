#coding:utf-8

#L'algorithme suivant donne le graphe (représenté comme une liste d'arrêtes) obtenue comme la fusion de plusieurs graphes.
def verification (fusions, blocs_de_qubits):##Un bloc de qubits est une liste d'arrêtes
    for couple in fusions:
        bloc_retenu_1, bloc_retenu_2 = None,None
        qubit1, qubit2 = couple[0],couple[1]

        for i in range(len(blocs_de_qubits)):
            for j in range(len(blocs_de_qubits)):
                bloc1 = blocs_de_qubits[i]
                bloc2 = blocs_de_qubits[j]
                for arrête_1 in bloc1:
                    for arrête_2 in bloc2:
                        if qubit1 in arrête_1:
                            bloc_retenu_1 = i
                            if qubit2 in arrête_2 :
                                bloc_retenu_2 = j ##on peut ajouter une arête une fois les blocs trouvés
        
        #On cherche les arêtes qui contiennent des noeuds à fusionner
        for k in range(len(blocs_de_qubits[bloc_retenu_1])):
            for l in range(len(blocs_de_qubits[bloc_retenu_2])):
                
                arrête1 = blocs_de_qubits[bloc_retenu_1][k]
                arrête2 = blocs_de_qubits[bloc_retenu_2][l]

                if arrête1[0] == qubit1 or arrête1[1] == qubit1:
                    blocs_de_qubits[bloc_retenu_1].pop(k)
                if arrête2[0] == qubit2 or arrête2[1] == qubit2:
                    blocs_de_qubits[bloc_retenu_2].pop(l)



                if arrête1[0] == qubit1 and arrête2[0] == qubit2:
                    bloc_fusionne.append([arrête1[1], arrête2[1]])
                if arrête1[0] == qubit1 and arrête2[1] == qubit2:
                    bloc_fusionne.append([arrête1[1], arrête2[0]])
                if arrête1[1] == qubit1 and arrête2[0] == qubit2:
                    bloc_fusionne.append([arrête1[0], arrête2[1]])
                if arrête1[1] == qubit1 and arrête2[1] == qubit2:
                    bloc_fusionne.append([arrête1[0], arrête2[0]])

        
        if bloc_retenu_1 == bloc_retenu_2 :
            bloc_fusionne = blocs_de_qubits[bloc_retenu_1]
        else :
            bloc_fusionne = blocs_de_qubits[bloc_retenu_1]+blocs_de_qubits[bloc_retenu_2]
            


        if bloc_retenu_1 == bloc_retenu_2 :
            blocs_de_qubits.pop(bloc_retenu_1)
        else :
            blocs_de_qubits.pop(max(bloc_retenu_1,bloc_retenu_2))
            blocs_de_qubits.pop(min(bloc_retenu_1,bloc_retenu_2))
        
        blocs_de_qubits.append(bloc_fusionne)
    return blocs_de_qubits##il n'y a plus que les arrêtes du graphe



blocs_de_qubits = [[(0,1),(1,2)],[(3,4),(4,5)]]
fusions = [(2,3)]

print(verification(fusions, blocs_de_qubits))