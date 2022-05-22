import sys
input=sys.stdin.readline

sudoku=[]
emptyspace=[]
rowcheck=[[False]*10 for _ in range(9)]
colcheck=[[False]*10 for _ in range(9)]
sqcheck=[[False]*10 for _ in range(9)]
for i in range(9):
    sudoku.append(list(map(int, input().rstrip())))
    for j in range(9):
        num=sudoku[i][j]
        if num:
            rowcheck[i][num]=True
            colcheck[j][num]=True
            sqcheck[(i//3)*3+j//3][num]=True
        else: emptyspace.append((i,j)) 

def fill(count):
    if count==len(emptyspace):
        for s in sudoku:
            print(''.join(map(str,s)))
        exit()
    i,j=emptyspace[count]
    for n in range(1,10):
        if rowcheck[i][n] or colcheck[j][n] or sqcheck[(i//3)*3+j//3][n]: continue
        sudoku[i][j]=n
        rowcheck[i][n]=True
        colcheck[j][n]=True
        sqcheck[(i//3)*3+j//3][n]=True
        fill(count+1)
        sudoku[i][j]=0
        rowcheck[i][n]=False
        colcheck[j][n]=False
        sqcheck[(i//3)*3+j//3][n]=False
fill(0)