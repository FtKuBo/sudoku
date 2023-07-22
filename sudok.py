def chiffreligne(i,puzzle):
    
    return [chf for chf in puzzle[i] if chf > 0]
    
def chiffrecolonne(i,y,puzzle):
    
    return [puzzle[o][y] for o in range(len(puzzle)) if puzzle[o][y] > 0]

def chiffrebloc(i,y,puzzle):
    
    chiffre_bloc=[]
    
    if 0 <= i < 3:
        if 0 <= y < 3:
            for w in range(3):
                chiffre_bloc+=puzzle[w][:3]
        if 3 <= y < 6:
            for w in range(3,6):
                chiffre_bloc+=puzzle[w][:3]
        if 6 <= y < 9:
            for w in range(6,9):
                chiffre_bloc+=puzzle[w][:3]

    if 3 <= i < 6:
        if 0 <= y < 3:
            for w in range(3):
                chiffre_bloc+=puzzle[w][3:6]
        if 3 <= y < 6:
            for w in range(3,6):
                chiffre_bloc+=puzzle[w][3:6]
        if 6 <= y < 9:
            for w in range(6,9):
                chiffre_bloc+=puzzle[w][3:6]
                        
    if 6 <= i < 9:
        if 0 <= y < 3:
            for w in range(3):
                chiffre_bloc+=puzzle[w][6:9]
        if 3 <= y < 6:
            for w in range(3,6):            
                chiffre_bloc+=puzzle[w][6:9]
        if 6 <= y < 9:
            for w in range(6,9):
                chiffre_bloc+=puzzle[w][6:9]
                        
                        
    while 0 in chiffre_bloc:
        chiffre_bloc.remove(0)
        
    return chiffre_bloc


def listfin(L):
    FL=[]
    for elt in L:
        if not elt in FL:
            FL.append(elt)
    FL.sort()
    return FL


def casesuivante(tuple,puzzle):
    
    for i in range(tuple[0],len(puzzle)):
        for y in range(len(puzzle[0])):
            if puzzle[i][y] == 0:
                return i, y
    return None


# si ça marche pas t'as pas le choix de te rabattre sur de la récursivié

def parcours(casee,puzzle):
    
    chiffre = [1,2,3,4,5,6,7,8,9]
    
    FL=listfin(chiffrebloc(casee[0],casee[1],puzzle)+chiffreligne(casee[0],puzzle)+chiffrecolonne(casee[0],casee[1],puzzle))   
    
    for elt in chiffre:
        
        if not elt in FL:
            
            puzzle[casee[0]][casee[1]] = elt
    
    rempli={casee:FL}
    
    print(rempli)
    
    suiv=casesuivante(casee,puzzle)
    
    while suiv :
        
        i, y = suiv
        
        L = chiffrebloc(i,y,puzzle)+chiffreligne(i,puzzle)+chiffrecolonne(i,y,puzzle)

        FL = listfin(L)
        
        print(FL)
        
        for elt in chiffre:
            
            if elt not in FL:
                
                puzzle[i][y] = elt
                
        if puzzle[i][y] == 0:
            
            print("il y a un probléme ")
            #j'arrive pas à me concentrer trouve une solution si non récursivité
            break
            
        else:        
        
            rempli[suiv] = FL
            
            print(rempli)
        
            suiv=casesuivante(suiv,puzzle)
    
    return puzzle
        
        
        
    
    
            



def sudoku(puzzle):
    
    for i in range(len(puzzle)):
        for y in range(len(puzzle[i])):
            
            if puzzle[i][y]==0:

                L = chiffrebloc(i,y,puzzle)+chiffreligne(i,puzzle)+chiffrecolonne(i,y,puzzle)

                FL = listfin(L)
                
                casee=(i, y)
                
                break
        else:
            continue
        break
    
    parcours(casee, puzzle)
    
            
    print(puzzle)
        
        
        
        
        
    return puzzle
# créer une boucle qui ne se stoppe que si il n'ya plus de 0 dans la grille
# si il n'ya plus d'element dans FL on revient en arriére jusqu'à ce qui est plus de deux issues
#labyrinthe exemple