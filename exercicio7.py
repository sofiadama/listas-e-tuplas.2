N = [int(input())]

print('0º =',*N)
for i in range(1,11):
    N.append(N[-1]*2)
    print(f'{i}º = {N[i]}') 
