m=int(input("enter row: "))
n=int(input("Enter col: "))
mat=[]
for i in range(m):
    mat.append([])
    for j in range(n):
        mat[i].append(j)
        mat[i][j]=int(input())
#for printing:        
for i in range(m):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()
'''INPUT:
enter row:3
enter col:2
1
2
3
4
6
8
OUTPUT:
1 2
3 4
5 6
'''
