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
#=============================================================================================
m=int(input("enter no. of row"))
n=int(input("enter no. of col"))
mat=[]
for i in range(m):
    ma=list(map(int,input().split()))
    mat.append(ma)
for i in range(m):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()
'''
INPUT:
3
4
2 4 7 8                                                                                                                         
2 5 8 7                                                                                                                         
6 9 7 1 

OUTPUT:
2 4 7 8                                                                                                                         
2 5 8 7                                                                                                                         
6 9 7 1
'''
#=============================================================================================
