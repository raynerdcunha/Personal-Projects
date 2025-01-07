import sys

#Pre-Defined

R1=[
    [' ',' ',' ',' ','8',' ',' ','4',' '],
    [' ',' ',' ',' ',' ','5',' ',' ','8'],
    ['8',' ',' ',' ',' ',' ',' ',' ','3'],
    ['1',' ',' ',' ',' ','8',' ','9',' '],
    [' ',' ','7','2','4','9','8',' ','5'],
    [' ','8','9',' ',' ',' ','7','3',' '],
    [' ',' ',' ',' ',' ','7',' ',' ',' '],
    [' ','2',' ','8',' ',' ',' ',' ',' '],
    ['4','9','5',' ','6',' ','2','8',' ']
    ]

#Main

def solve():
    for i in range(9):
        for j in range(9):
            if R1[i][j]==' ':
                for k in range(1,10):
                    if check(i,j,str(k)):
                        R1[i][j]=str(k)
                        solve()
                        R1[i][j]=' '
                return
    display(R1)

def check(i1,j1,k1):
    global R1
    for a in range(9):
        if R1[i1][a]==k1:
            return False
    for a1 in range(9):
        if R1[a1][j1]==k1:
            return False
    i2=(i1//3)*3
    j2=(j1//3)*3
    for b in range(3):
        for c in range(3):
            if R1[i2+b][j2+c]==k1:
                return False
    return True

def display(R):
    for r in range(0,9,1):
        print('+---+---+---+  +---+---+---+  +---+---+---+')
        print('| ',end='')
        for b in range(0,3,1):
                for e in range(0,3,1):
                    print(R[r][b+e],end=' | ')
                if b!=2:
                    print(' | ',end='')
        print()
        if r==2 or r==5:
            print('+---+---+---+  +---+---+---+  +---+---+---+')
            print()
    print('+---+---+---+  +---+---+---+  +---+---+---+')
    sys.exit()

#Initiation
    
solve()
