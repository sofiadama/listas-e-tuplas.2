1172

X = list(map(int,input().split()))[:10]

for i in range(len(X)):
     if X[i] < 1:
          X[i] = 1 

print(f‘[X{i}] = {X[i]}’) 
