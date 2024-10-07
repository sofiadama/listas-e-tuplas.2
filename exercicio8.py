X = list(map(int,input().split()))[:5]

for i in range(len(X)):
    if i == 0:
        print(X[i] + X[i+1])
    elif i == 4:
        print(X[i] + X[i-1])
    else:  
        print(X[i-1] + X[i] + X[i+1])
      
