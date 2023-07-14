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
        for y in range(tuple[1]+1,len(puzzle[0])):
            if puzzle[i][y] == 0:
                return i, y
            



def sudoku(puzzle):
    
    chiffre=[1,2,3,4,5,6,7,8,9]
    
    for i in range(len(puzzle)):
        
        chiffre_ligne = chiffreligne(i,puzzle)

        for y in range(len(puzzle[i])):
            
            chiffre_colonne = chiffrecolonne(i,y,puzzle)
            
            chiffre_bloc = chiffrebloc(i,y,puzzle)
            
            L = chiffre_bloc+chiffre_ligne+chiffre_colonne
            
            FL = listfin(L)

    print(casesuivante((0,3),puzzle))
            
    print(puzzle)
        
        
        
        
        
    return puzzle