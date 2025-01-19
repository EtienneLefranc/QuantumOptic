#coding:utf-8


#On se donne un graphe représenté par ses listes d'adjacence. Les sommets sont indexés par des indices :
#Par exemple :
g = [[1],[0,2,3,8],[1,3],[1,2,4],[3,5],[4,6],[7,8,9,10],[6,8],[1,6,7],[6],[6]]

#Le résultat final prend la forme d'une liste [] de taille 
#le nombre de chaînes que l'on veut fusionner et chaque élément est la taille d'une chaîne.
#et d'une liste de fusions ((numero_element1,indice_element1),(numero_element2,indice_element2))

def simplification(tailles,fusions):
    #On supposera que l'algorithme a donné des fusions de telle sorte qu'un même noeud ne soit pas fusionné 2 fois
    nouvelles_tailles = [x for x in tailles]
    nouvelles_fusions = [x for x in fusions]
    print(nouvelles_tailles,nouvelles_fusions)
    sent = True
    while sent :
        i = 0
        nbr = len(nouvelles_fusions) #la taille fixe
        while i < len(nouvelles_fusions) :
            fus = nouvelles_fusions[i]
            
            n1,i1 = fus[0]
            t1 = nouvelles_tailles[n1] #la taille actuelle de la liste n1
            n2,i2 = fus[1]
            t2 = nouvelles_tailles[n2] #la taille actuelle de la liste n2

            if n1 != n2 : 
                #Sinon aucune simplification n'est possible, et ce cas risquerait de causer des problèmes
                #par la suite
            
                if i1 == 0 and i2 == 0 :
                    #print("i1 == 0 and i2 == 0")
                    #mise à jour des tailles de listes :
                    #on supprime n1 pour le mettre dans n2 : On fait la même opération que pour la boucle suivante
                    #en inversant 1 et 2
                    nouvelles_tailles[n1] = 0
                    nouvelles_tailles[n2] = t1+t2- 2

                    _ = nouvelles_fusions.pop(i)
                    #mise à  jour des autres : On remplace (n1,i) par (n2,t1 - 1 - i) (pour i > 0)
                    #et                        on remplace (n2,i) par (n2,t1 -2 + i) (pour i > 0)  
                    for j in range(len(nouvelles_fusions)):
                        ffus = nouvelles_fusions[j]
                        nn1,ii1 = ffus[0]
                        nn2,ii2 = ffus[1]

                        if nn1 == n1 :
                            ii1 = t1 - 1 - ii1
                            nn1 = n2
                        elif nn1 == n2 :
                            ii1 = ii1 + t1 - 2
                        
                        if nn2 == n1 :
                            ii2 = t1 - 1 - ii2
                            nn2 = n2
                        elif nn2 == n2 :
                            ii2 = ii2 + t1 - 2

                        nouvelles_fusions[j] = ((nn1,ii1),(nn2,ii2))
                    
                    i-=1    
                    #print(nouvelles_tailles,nouvelles_fusions)
                

                if i1 == 0 and i2 == t2 - 1 and i2 != 0 : #Pour écarter le cas où i2 = t2 - 1 =0
                    #print("i1 == 0 and i2 == t2 - 1 and i2 != 0")
                    #mise à jour des tailles de listes :
                    #on supprime n1 pour le mettre dans n2 : On fait la même opération que pour la boucle suivante
                    #en inversant 1 et 2
                    nouvelles_tailles[n1] = 0
                    nouvelles_tailles[n2] = t1+t2- 2

                    _ = nouvelles_fusions.pop(i)
                    #mise à  jour des autres : On remplcae (n1,i) par (n2,i+(t2-2)) (pout i > 0)
                    for j in range(len(nouvelles_fusions)):
                        ffus = nouvelles_fusions[j]
                        nn1,ii1 = ffus[0]
                        nn2,ii2 = ffus[1]
                        if nn1 == n1 :
                            ii1 = ii1 + t2 - 2
                            nn1 = n2
                        if nn2 == n1 :
                            ii2 = ii2 + t2 - 2
                            nn2 = n2
                        nouvelles_fusions[j] = ((nn1,ii1),(nn2,ii2))
                    
                    i -= 1
                    #print(nouvelles_tailles,nouvelles_fusions)


                        

                if i1 == t1-1  and i2 == 0 and i1 != 0: #Pour écarter le cas où i1 = 0 = t1 -1
                    #print("i1 == t1-1  and i2 == 0 and i1 != 0")
                    #mise à jour des tailles de listes :
                    #on supprime n2 pour le mettre dans n1 :
                    nouvelles_tailles[n2] = 0
                    nouvelles_tailles[n1] = t1+t2- 2

                    _ = nouvelles_fusions.pop(i)
                    #mise à  jour des autres : On remplcae (n2,i) par (n1,i+(t1-2))
                    for j in range(len(nouvelles_fusions)):
                        ffus = nouvelles_fusions[j]
                        nn1,ii1 = ffus[0]
                        nn2,ii2 = ffus[1]
                        if nn1 == n2 :
                            ii1 = ii1 + t1 - 2
                            nn1 = n1
                        if nn2 == n2 :
                            ii2 = ii2 + t1 - 2
                            nn2 = n1
                        nouvelles_fusions[j] = ((nn1,ii1),(nn2,ii2))
                    
                    i -= 1
                    #print(nouvelles_tailles,nouvelles_fusions)
                        


                if i1 == t1-1 and i2 == t2 -1 : #Pour écarter le cas où i1 = 0 = t1 -1 et i2 = 0 = t2 - 1 
                    #print("i1 == t1-1 and i2 == t2 -1")
                    #mise à jour des tailles de listes :
                    #on supprime n2 pour le mettre dans n1 : On fait la même opération que pour la boucle suivante
                    #en inversant 1 et 2
                    nouvelles_tailles[n1] = t1+t2- 2
                    nouvelles_tailles[n2] = 0

                    _ = nouvelles_fusions.pop(i)
                    #mise à  jour des autres : On ne change pas (n1,i)) (pour i < t1 -1)
                    #et                        on remplace (n2,i) par (n1,(t1-1) + (t2-2-i)) (pour i < t2 -1) 
                    for j in range(len(nouvelles_fusions)):
                        ffus = nouvelles_fusions[j]
                        nn1,ii1 = ffus[0]
                        nn2,ii2 = ffus[1]
                        if nn1 == n2 :
                            ii1 = (t1-1) + (t2-2-ii1)
                            nn1 = n1
                        if nn2 == n2 :
                            ii2 = (t1-1) + (t2-2-ii2)
                            nn2 = n1
                        nouvelles_fusions[j] = ((nn1,ii1),(nn2,ii2))
                    
                    i -= 1
                    #print(nouvelles_tailles,nouvelles_fusions)

            i += 1 
            #Si on a trouvé une fusion, on a pas besoin d'incrémenter i, 
            #c'est pour cela qu'on lui a soustrait 1 précédemment

        if nbr == len(nouvelles_fusions) : #si on a pas retiré de fusion
            sent = False



    return nouvelles_tailles, nouvelles_fusions

if __name__ == "__main__" :
    #print(simplification([4,3,3],[((0,0),(1,2)),((1,1),(2,2)),((0,3),(2,0))]))
    #print(simplification([1,3,3,3,4,3,4,3],[((0,0),(1,0)),((1,1),(2,0)),((1,2),(3,2)),\
    #    ((2,2),(4,0)),((3,0),(4,3)),((3,1),(5,2)),((4,2),(7,0)),((5,0),(6,0)),((6,3),(7,2))]))
    #print(simplification([1,3],[((0,0),(1,0))]))
    print(simplification([3, 3, 4],[((0, 0), (1, 0)), ((0, 1), (2, 0)), ((1, 2), (2, 3))]))