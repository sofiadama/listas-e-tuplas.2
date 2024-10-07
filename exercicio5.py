1743
X = list(map(int,input().split()))[:5]
Y = list(map(int,input().split()))[:5]

for i in range(len(X)):
     if X[i] > 1 and Y[i] > 1:
           print(‘Valores inválidos!’)
     elif X[i] != Y[i]:
           print(‘S’)
     else: 
           print(‘N’)
