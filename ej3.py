'''
Retorna la transpuesta de un matriz con una lambda

[[1,2,3],
 [4,5,6],
 [7,8,9]]

deberia quedar:

[[1,4,7],
 [2,5,8],
 [3,6,9]]


'''

M1 = [[1,2,3],
     [4,5,6],
     [7,8,9]] 


M2 = [[10,20,30],
     [40,50,60],
     [70,80,90]] 


M3 = [[2,7,9,4],
      [6,1,2,3],
      [0,3,4,5],
      [1,3,8,0],
      ] 

print(f"\nResult: { (lambda a: [[a[i][j] for i in range(len(a[j]))] for j in range(len(a))])(M1) }")
print(f"\nResult: { (lambda a: [[a[i][j] for i in range(len(a[j]))] for j in range(len(a))])(M2) }")
print(f"\nResult: { (lambda a: [[a[i][j] for i in range(len(a[j]))] for j in range(len(a))])(M3) }")
